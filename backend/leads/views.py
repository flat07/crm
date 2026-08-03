# backend/leads/views.py
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import decorators, response, status, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated

from leads import selectors, services

from .filters import LeadFilter
from .permissions import (
    CanCreateLead,
    CanDeleteLead,
    CanUpdateLead,
    CanViewLead,
)
from .serializers import LeadSerializer


class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeadSerializer

    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )

    filterset_class = LeadFilter

    search_fields = (
        "title",
        "company__name",
        "contact__first_name",
        "contact__last_name",
        "description",
    )

    ordering_fields = (
        "title",
        "estimated_value",
        "probability",
        "expected_close_date",
        "created_at",
    )

    ordering = ("-created_at",)

    permission_classes = (IsAuthenticated,)

    permission_classes_by_action = {  # noqa: RUF012
        "list": (CanViewLead,),
        "retrieve": (CanViewLead,),
        "create": (CanCreateLead,),
        "update": (CanUpdateLead,),
        "partial_update": (CanUpdateLead,),
        "destroy": (CanDeleteLead,),
        "restore": (CanDeleteLead,),
        "hard_delete": (CanDeleteLead,),
    }

    def get_permissions(self):
        permission_classes = self.permission_classes_by_action.get(
            self.action,
            self.permission_classes,
        )
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        return selectors.lead_list()

    def perform_create(self, serializer):
        serializer.instance = services.create_lead(
            **serializer.validated_data,
        )

    def perform_update(self, serializer):
        serializer.instance = services.update_lead(
            lead=self.get_object(),
            **serializer.validated_data,
        )

    def perform_destroy(self, instance):
        services.archive(
            lead=instance,
        )

    @decorators.action(
        detail=True,
        methods=["post"],
    )
    def restore(self, request, pk=None):
        lead = self.get_object()

        services.restore(
            lead=lead,
        )

        return response.Response(
            self.get_serializer(lead).data,
            status=status.HTTP_200_OK,
        )

    @decorators.action(
        detail=True,
        methods=["delete"],
    )
    def hard_delete(self, request, pk=None):
        lead = self.get_object()

        services.delete(
            lead=lead,
        )

        return response.Response(
            status=status.HTTP_204_NO_CONTENT,
        )
