# backend/contacts/views.py
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import decorators, response, status, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated

from contacts import selectors, services

from .filters import ContactFilter
from .permissions import (
    CanCreateContact,
    CanDeleteContact,
    CanUpdateContact,
    CanViewContact,
)
from .serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer

    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )

    filterset_class = ContactFilter

    search_fields = (
        "first_name",
        "last_name",
        "email",
        "phone",
        "mobile",
        "job_title",
        "company__name",
        "owner__first_name",
        "owner__last_name",
        "city",
        "country",
    )

    ordering_fields = (
        "first_name",
        "last_name",
        "created_at",
        "birthday",
    )
    ordering = (
        "first_name",
        "last_name",
    )

    permission_classes = (IsAuthenticated,)

    permission_classes_by_action = {  # noqa: RUF012
        "list": (CanViewContact,),
        "retrieve": (CanViewContact,),
        "create": (CanCreateContact,),
        "update": (CanUpdateContact,),
        "partial_update": (CanUpdateContact,),
        "destroy": (CanDeleteContact,),
        "restore": (CanDeleteContact,),
        "hard_delete": (CanDeleteContact,),
    }

    def get_permissions(self):
        permission_classes = self.permission_classes_by_action.get(
            self.action,
            self.permission_classes,
        )
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        return selectors.contact_list()

    def perform_create(self, serializer):
        serializer.instance = services.create_contact(
            **serializer.validated_data,
        )

    def perform_update(self, serializer):
        serializer.instance = services.update_contact(
            contact=self.get_object(),
            **serializer.validated_data,
        )

    def perform_destroy(self, instance):
        services.archive(
            contact=instance,
        )

    @decorators.action(
        detail=True,
        methods=["post"],
    )
    def restore(self, request, pk=None):
        contact = self.get_object()

        services.restore(
            contact=contact,
        )

        return response.Response(
            self.get_serializer(contact).data,
            status=status.HTTP_200_OK,
        )

    @decorators.action(
        detail=True,
        methods=["delete"],
    )
    def hard_delete(self, request, pk=None):
        contact = self.get_object()

        services.delete(
            contact=contact,
        )

        return response.Response(
            status=status.HTTP_204_NO_CONTENT,
        )
