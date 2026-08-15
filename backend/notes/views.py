# backend/notes/views.py

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import decorators, response, status, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated

from notes import selectors, services

from .filters import NoteFilter
from .permissions import (
    CanCreateNote,
    CanDeleteNote,
    CanUpdateNote,
    CanViewNote,
)
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer

    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )

    filterset_class = NoteFilter

    search_fields = (
        "title",
        "content",
        "created_by__first_name",
        "created_by__last_name",
    )

    ordering_fields = (
        "title",
        "is_pinned",
        "is_private",
        "created_at",
        "updated_at",
    )

    ordering = (
        "-is_pinned",
        "-created_at",
    )

    permission_classes = (IsAuthenticated,)

    permission_classes_by_action = {  # noqa: RUF012
        "list": (CanViewNote,),
        "retrieve": (CanViewNote,),
        "create": (CanCreateNote,),
        "update": (CanUpdateNote,),
        "partial_update": (CanUpdateNote,),
        "destroy": (CanDeleteNote,),
        "restore": (CanDeleteNote,),
        "hard_delete": (CanDeleteNote,),
    }

    def get_permissions(self):
        permission_classes = self.permission_classes_by_action.get(
            self.action,
            self.permission_classes,
        )

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        return selectors.note_list()

    def perform_create(self, serializer):
        serializer.instance = services.create_note(
            **serializer.validated_data,
            created_by=self.request.user,
        )

    def perform_update(self, serializer):
        serializer.instance = services.update_note(
            note=self.get_object(),
            **serializer.validated_data,
        )

    def perform_destroy(self, instance):
        services.archive(
            note=instance,
        )

    @decorators.action(
        detail=True,
        methods=["post"],
    )
    def restore(self, request, pk=None):
        note = selectors.note_detail_with_deleted(pk)

        services.restore(
            note=note,
        )

        return response.Response(
            self.get_serializer(note).data,
            status=status.HTTP_200_OK,
        )

    @decorators.action(
        detail=True,
        methods=["delete"],
    )
    def hard_delete(self, request, pk=None):
        note = self.get_object()

        services.delete_note(
            note=note,
        )

        return response.Response(
            status=status.HTTP_204_NO_CONTENT,
        )

    @decorators.action(
        detail=True,
        methods=["post"],
    )
    def toggle_pin(self, request, pk=None):
        note = self.get_object()

        services.toggle_pin(
            note=note,
        )

        return response.Response(
            self.get_serializer(note).data,
            status=status.HTTP_200_OK,
        )

    @decorators.action(
        detail=True,
        methods=["post"],
    )
    def toggle_private(self, request, pk=None):
        note = self.get_object()

        services.toggle_private(
            note=note,
        )

        return response.Response(
            self.get_serializer(note).data,
            status=status.HTTP_200_OK,
        )
