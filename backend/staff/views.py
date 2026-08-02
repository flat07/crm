# backend/staff/views.py
from rest_framework.viewsets import ModelViewSet

from . import selectors, services
from .permissions import IsAdmin
from .serializers import (
    UserCreateSerializer,
    UserDetailSerializer,
    UserListSerializer,
    UserUpdateSerializer,
)


class UserViewSet(ModelViewSet):
    permission_classes = (IsAdmin,)

    def get_queryset(self):
        return selectors.user_list()

    def get_serializer_class(self):

        if self.action == "list":
            return UserListSerializer

        if self.action == "retrieve":
            return UserDetailSerializer

        if self.action == "create":
            return UserCreateSerializer

        return UserUpdateSerializer

    def perform_create(
        self,
        serializer,
    ):

        services.create_user(
            **serializer.validated_data,
        )

    def perform_update(
        self,
        serializer,
    ):

        services.update_user(
            user=self.get_object(),
            **serializer.validated_data,
        )
