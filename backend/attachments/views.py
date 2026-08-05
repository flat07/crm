# backend/attachments/views.py

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import decorators, filters, response, status, viewsets
from rest_framework.permissions import IsAuthenticated

from attachments import selectors, services
from attachments.filters import AttachmentFilter
from attachments.serializers import AttachmentSerializer

from .permissions import (
    CanCreateAttachment,
    CanDeleteAttachment,
    CanUpdateAttachment,
    CanViewAttachment,
)


class AttachmentViewSet(viewsets.ModelViewSet):
    serializer_class = AttachmentSerializer

    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )

    filterset_class = AttachmentFilter

    search_fields = (
        "filename",
        "description",
        "mime_type",
    )

    ordering_fields = (
        "created_at",
        "filename",
        "file_size",
    )

    ordering = ("-created_at",)

    permission_classes = (IsAuthenticated,)

    permission_classes_by_action = {  # noqa: RUF012
        "list": (CanViewAttachment,),
        "retrieve": (CanViewAttachment,),
        "create": (CanCreateAttachment,),
        "update": (CanUpdateAttachment,),
        "partial_update": (CanUpdateAttachment,),
        "destroy": (CanDeleteAttachment,),
        "restore": (CanDeleteAttachment,),
        "hard_delete": (CanDeleteAttachment,),
    }

    def get_permissions(self):
        permission_classes = self.permission_classes_by_action.get(
            self.action,
            self.permission_classes,
        )
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        return selectors.attachment_list()

    def perform_create(self, serializer):
        serializer.instance = services.create_attachment(
            user=self.request.user,
            **serializer.validated_data,
        )

    def perform_update(self, serializer):
        serializer.instance = services.update_attachment(
            attachment=self.get_object(),
            **serializer.validated_data,
        )

    def perform_destroy(self, instance):
        services.archive(
            attachment=instance,
        )

    @decorators.action(
        detail=True,
        methods=["post"],
    )
    def restore(self, request, pk=None):
        attachment = self.get_object()

        services.restore(
            attachment=attachment,
        )

        return response.Response(
            self.get_serializer(attachment).data,
            status=status.HTTP_200_OK,
        )

    @decorators.action(
        detail=True,
        methods=["delete"],
    )
    def hard_delete(self, request, pk=None):
        attachment = self.get_object()

        services.delete(
            attachment=attachment,
        )

        return response.Response(
            status=status.HTTP_204_NO_CONTENT,
        )
