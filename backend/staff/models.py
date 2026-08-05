# backend/staff/models.py

from __future__ import annotations

from typing import ClassVar

from common.models import BaseModel
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.db import models
from django.utils.functional import cached_property

from .managers import UserManager


class Department(BaseModel):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name


class Permission(BaseModel):
    code = models.CharField(
        max_length=100,
        unique=True,
    )

    name = models.CharField(
        max_length=255,
    )

    description = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ("code",)

    def __str__(self) -> str:
        return self.name


class Role(BaseModel):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    permissions = models.ManyToManyField(
        Permission,
        related_name="roles",
    )

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(
        unique=True,
    )

    first_name = models.CharField(
        max_length=150,
        blank=True,
    )

    last_name = models.CharField(
        max_length=150,
        blank=True,
    )

    phone = models.CharField(
        max_length=40,
        blank=True,
    )

    job_title = models.CharField(
        max_length=150,
        blank=True,
    )

    avatar = models.ImageField(
        upload_to="avatars/",
        blank=True,
        null=True,
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users",
    )

    roles = models.ManyToManyField(
        Role,
        related_name="users",
    )

    is_staff = models.BooleanField(
        default=False,
    )

    last_login = models.DateTimeField(
        null=True,
        blank=True,
    )

    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS: ClassVar[list[str]] = []

    class Meta:
        ordering = (
            "first_name",
            "last_name",
        )

    def __str__(self):
        return self.email

    def get_full_name(self):

        return (f"{self.first_name} {self.last_name}").strip()

    def has_role(
        self,
        role_name: str,
    ):

        return self.roles.filter(name=role_name).exists()

    @cached_property
    def permission_codes(self):
        return set(
            self.roles.values_list(
                "permissions__code",
                flat=True,
            ).distinct()
        )

    def has_permission(self, permission_code):
        return permission_code in self.permission_codes
