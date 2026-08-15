# backend/notes/models.py
from __future__ import annotations

from common.models import BaseModel
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Note(BaseModel):
    title = models.CharField(
        max_length=255,
        blank=True,
    )

    content = models.TextField()

    created_by = models.ForeignKey(
        "staff.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="notes",
    )

    is_pinned = models.BooleanField(
        default=False,
    )

    is_private = models.BooleanField(
        default=False,
    )

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
    )

    object_id = models.UUIDField()

    content_object = GenericForeignKey(
        "content_type",
        "object_id",
    )

    class Meta:
        ordering = (
            "-is_pinned",
            "-created_at",
        )
        indexes = (
            models.Index(fields=["content_type", "object_id"]),
            models.Index(fields=["created_by"]),
        )

    def __str__(self):
        return self.title or f"Note {self.pk}"
