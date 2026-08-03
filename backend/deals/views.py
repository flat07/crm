# backend/deals/views.py
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import decorators, response, status, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated

from deals import selectors, services

from .filters import DealFilter
from .permissions import (
    CanCreateDeal,
    CanDeleteDeal,
    CanUpdateDeal,
    CanViewDeal,
)
from .serializers import DealSerializer


class DealViewSet(viewsets.ModelViewSet):
    serializer_class = DealSerializer

    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )
    filterset_class = DealFilter

    search_fields = (
        "company__name",
        "contact__first_name",
        "contact__last_name",
        "description",
    )

    ordering_fields = (
        "amount",
        "probability",
        "expected_close_date",
        "created_at",
    )

    ordering = ("-created_at",)

    permission_classes = (IsAuthenticated,)

    permission_classes_by_action = {  # noqa: RUF012
        "list": (CanViewDeal,),
        "retrieve": (CanViewDeal,),
        "create": (CanCreateDeal,),
        "update": (CanUpdateDeal,),
        "partial_update": (CanUpdateDeal,),
        "destroy": (CanDeleteDeal,),
        "restore": (CanDeleteDeal,),
        "hard_delete": (CanDeleteDeal,),
    }

    def get_permissions(self):
        permission_classes = self.permission_classes_by_action.get(
            self.action,
            self.permission_classes,
        )
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        return selectors.deal_list()

    def perform_create(self, serializer):
        serializer.instance = services.create_deal(
            **serializer.validated_data,
        )

    def perform_update(self, serializer):
        serializer.instance = services.update_deal(
            deal=self.get_object(),
            **serializer.validated_data,
        )

    def perform_destroy(self, instance):
        services.archive(
            deal=instance,
        )

    @decorators.action(
        detail=True,
        methods=["post"],
    )
    def restore(self, request, pk=None):
        deal = self.get_object()

        services.restore(
            deal=deal,
        )

        return response.Response(
            self.get_serializer(deal).data,
            status=status.HTTP_200_OK,
        )

    @decorators.action(
        detail=True,
        methods=["delete"],
    )
    def hard_delete(self, request, pk=None):
        deal = self.get_object()

        services.delete(
            deal=deal,
        )

        return response.Response(
            status=status.HTTP_204_NO_CONTENT,
        )
