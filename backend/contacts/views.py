# backend/contacts/views.py
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import decorators, response, status, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated

from contacts import selectors, services

from .filters import (
    ContactEmailFilter,
    ContactFilter,
    ContactPhoneFilter,
    ContactTagAssignmentFilter,
    ContactTagFilter,
)
from .models import ContactEmail, ContactPhone, ContactTag, ContactTagAssignment
from .permissions import (
    CanCreateContact,
    CanDeleteContact,
    CanUpdateContact,
    CanViewContact,
)
from .serializers import (
    ContactEmailSerializer,
    ContactPhoneSerializer,
    ContactSerializer,
    ContactTagAssignmentSerializer,
    ContactTagSerializer,
)


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
        contact = selectors.contact_detail_with_deleted(pk)

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


class ContactTagViewSet(viewsets.ModelViewSet):
    queryset = ContactTag.objects.all()

    serializer_class = ContactTagSerializer

    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )

    filterset_class = ContactTagFilter

    search_fields = ("name",)

    ordering_fields = (
        "name",
        "created_at",
    )

    ordering = ("name",)

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
        return selectors.contact_tag_list()

    def perform_create(self, serializer):
        serializer.instance = services.create_contact_tag(
            **serializer.validated_data,
        )

    def perform_update(self, serializer):
        serializer.instance = services.update_contact_tag(
            contact_tag=self.get_object(),
            **serializer.validated_data,
        )

    def perform_destroy(self, instance):
        services.archive_contact_tag(
            contact_tag=instance,
        )

    @decorators.action(
        detail=True,
        methods=["post"],
    )
    def restore(self, request, pk=None):
        contact_tag = self.get_object()

        services.restore_contact_tag(
            contact_tag=contact_tag,
        )

        return response.Response(
            self.get_serializer(contact_tag).data,
            status=status.HTTP_200_OK,
        )

    @decorators.action(
        detail=True,
        methods=["delete"],
    )
    def hard_delete(self, request, pk=None):
        contact_tag = self.get_object()

        services.delete_contact_tag(
            contact_tag=contact_tag,
        )

        return response.Response(
            status=status.HTTP_204_NO_CONTENT,
        )


class ContactEmailViewSet(viewsets.ModelViewSet):
    queryset = ContactEmail.objects.select_related("contact")

    serializer_class = ContactEmailSerializer

    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )

    filterset_class = ContactEmailFilter

    search_fields = ("email",)

    ordering_fields = (
        "email",
        "created_at",
    )

    ordering = ("-is_primary",)

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
        return selectors.contact_email_list()

    def perform_create(self, serializer):
        serializer.instance = services.create_contact_email(
            **serializer.validated_data,
        )

    def perform_update(self, serializer):
        serializer.instance = services.update_contact_email(
            instance=self.get_object(),
            **serializer.validated_data,
        )

    def perform_destroy(self, instance):
        services.archive_contact_email(
            instance=instance,
        )

    @decorators.action(
        detail=True,
        methods=["post"],
    )
    def restore(self, request, pk=None):
        instance = self.get_object()

        services.restore_contact_email(
            instance=instance,
        )

        return response.Response(
            self.get_serializer(instance).data,
            status=status.HTTP_200_OK,
        )

    @decorators.action(
        detail=True,
        methods=["delete"],
    )
    def hard_delete(self, request, pk=None):
        instance = self.get_object()

        services.delete_contact_email(
            instance=instance,
        )

        return response.Response(
            status=status.HTTP_204_NO_CONTENT,
        )


class ContactPhoneViewSet(viewsets.ModelViewSet):
    queryset = ContactPhone.objects.select_related("contact")

    serializer_class = ContactPhoneSerializer

    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )

    filterset_class = ContactPhoneFilter

    search_fields = ("phone",)

    ordering_fields = (
        "phone",
        "created_at",
    )

    ordering = ("-is_primary",)

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
        return selectors.contact_phone_list()

    def perform_create(self, serializer):
        serializer.instance = services.create_contact_phone(
            **serializer.validated_data,
        )

    def perform_update(self, serializer):
        serializer.instance = services.update_contact_phone(
            instance=self.get_object(),
            **serializer.validated_data,
        )

    def perform_destroy(self, instance):
        services.archive_contact_phone(
            instance=instance,
        )

    @decorators.action(
        detail=True,
        methods=["post"],
    )
    def restore(self, request, pk=None):
        instance = self.get_object()

        services.restore_contact_phone(
            instance=instance,
        )

        return response.Response(
            self.get_serializer(instance).data,
            status=status.HTTP_200_OK,
        )

    @decorators.action(
        detail=True,
        methods=["delete"],
    )
    def hard_delete(self, request, pk=None):
        instance = self.get_object()

        services.delete_contact_phone(
            instance=instance,
        )

        return response.Response(
            status=status.HTTP_204_NO_CONTENT,
        )


class ContactTagAssignmentViewSet(viewsets.ModelViewSet):
    queryset = ContactTagAssignment.objects.select_related(
        "contact",
        "tag",
    )

    serializer_class = ContactTagAssignmentSerializer

    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )

    filterset_class = ContactTagAssignmentFilter

    search_fields = (
        "contact__first_name",
        "contact__last_name",
        "tag__name",
    )

    ordering_fields = ("created_at",)

    ordering = ("-created_at",)

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
        return selectors.contact_assignment_list()

    def perform_create(self, serializer):
        serializer.instance = services.create_contact_assignment(
            **serializer.validated_data,
        )

    def perform_update(self, serializer):
        serializer.instance = services.update_contact_assignment(
            contact=self.get_object(),
            **serializer.validated_data,
        )

    def perform_destroy(self, instance):
        services.archive_contact_assignment(
            contact_assignment=instance,
        )

    @decorators.action(
        detail=True,
        methods=["post"],
    )
    def restore(self, request, pk=None):
        contact_assignment = self.get_object()

        services.restore_contact_assignment(
            contact_assignment=contact_assignment,
        )

        return response.Response(
            self.get_serializer(contact_assignment).data,
            status=status.HTTP_200_OK,
        )

    @decorators.action(
        detail=True,
        methods=["delete"],
    )
    def hard_delete(self, request, pk=None):
        contact_assignment = self.get_object()

        services.delete_contact_assignment(
            contact_assignment=contact_assignment,
        )

        return response.Response(
            status=status.HTTP_204_NO_CONTENT,
        )
