# backend/activities/views.py

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import decorators, response, status, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated

from activities import selectors, services

from .filters import ActivityFilter
from .permissions import (
    CanCreateActivity,
    CanDeleteActivity,
    CanUpdateActivity,
    CanViewActivity,
)
from .serializers import ActivitySerializer


class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer

    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )

    filterset_class = ActivityFilter

    search_fields = (
        "title",
        "description",
        "owner__first_name",
        "owner__last_name",
        "created_by__first_name",
        "created_by__last_name",
    )

    ordering_fields = (
        "title",
        "priority",
        "status",
        "activity_type",
        "due_date",
        "completed_at",
        "created_at",
    )

    ordering = (
        "-due_date",
        "-created_at",
    )

    permission_classes = (IsAuthenticated,)

    permission_classes_by_action = {  # noqa: RUF012
        "list": (CanViewActivity,),
        "retrieve": (CanViewActivity,),
        "create": (CanCreateActivity,),
        "update": (CanUpdateActivity,),
        "partial_update": (CanUpdateActivity,),
        "destroy": (CanDeleteActivity,),
        "restore": (CanDeleteActivity,),
        "hard_delete": (CanDeleteActivity,),
    }

    def get_permissions(self):
        permission_classes = self.permission_classes_by_action.get(
            self.action,
            self.permission_classes,
        )
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        return selectors.activity_list()

    def perform_create(self, serializer):
        serializer.instance = services.create_activity(
            **serializer.validated_data,
        )

    def perform_update(self, serializer):
        serializer.instance = services.update_activity(
            activity=self.get_object(),
            **serializer.validated_data,
        )

    def perform_destroy(self, instance):
        services.archive(
            activity=instance,
        )

    @decorators.action(
        detail=True,
        methods=["post"],
    )
    def restore(self, request, pk=None):
        activity = self.get_object()

        services.restore(
            activity=activity,
        )

        return response.Response(
            self.get_serializer(activity).data,
            status=status.HTTP_200_OK,
        )

    @decorators.action(
        detail=True,
        methods=["delete"],
    )
    def hard_delete(self, request, pk=None):
        activity = self.get_object()

        services.delete(
            activity=activity,
        )

        return response.Response(
            status=status.HTTP_204_NO_CONTENT,
        )
