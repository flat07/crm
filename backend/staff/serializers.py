# backend/staff/serializers.py
from typing import Any

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Department, User


class LoginSerializer(TokenObtainPairSerializer):
    username_field = "email"

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        typed_data: dict[str, Any] = data
        typed_data["user"] = UserDetailSerializer(
            self.user,
            context=self.context,
        ).data

        return data

    # {
    # "refresh": "",
    # "access": "",
    # "user": {
    #     "id": "df39ccfb-3a43-4d0b-a44e-6a3f52e3be58",
    #     "email": "admin@a.com",
    #     "first_name": "Admin",
    #     "last_name": "User",
    #     "department": {
    #     "id": "53f7f5bc-3d4b-41f9-8019-1b6c6e54bfa9",
    #     "name": "Administration"
    #     },
    #     "roles": [
    #     "Administrator"
    #     ],
    #     "avatar": null,
    #     "job_title": ""
    #     }
    # }


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()

    new_password = serializers.CharField()


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = (
            "id",
            "name",
        )


class UserListSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField()

    class Meta:
        model = User

        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "department",
            "is_active",
        )


class UserDetailSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(
        read_only=True,
    )

    roles = serializers.StringRelatedField(
        many=True,
    )

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "department",
            "roles",
            "avatar",
            "job_title",
        )


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
    )

    class Meta:
        model = User

        fields = (
            "email",
            "password",
            "first_name",
            "last_name",
            "phone",
            "department",
        )


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        exclude = ("password",)
