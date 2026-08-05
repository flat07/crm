# backend/attachments/models.py
from __future__ import annotations

import os

from common.models import BaseModel
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Attachment(BaseModel):
    file = models.FileField(
        upload_to="attachments/%Y/%m/",
    )

    filename = models.CharField(
        max_length=255,
    )

    description = models.TextField(
        blank=True,
    )

    mime_type = models.CharField(
        max_length=100,
        blank=True,
    )

    file_size = models.PositiveBigIntegerField(
        default=0,
    )

    uploaded_by = models.ForeignKey(
        "staff.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="attachments",
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
        ordering = ("-created_at",)

        indexes = (
            models.Index(fields=["content_type", "object_id"]),
            models.Index(fields=["uploaded_by"]),
        )

    def save(self, *args, **kwargs):
        if self.file:
            self.filename = os.path.basename(self.file.name)
            self.file_size = self.file.size

            if hasattr(self.file.file, "content_type"):
                self.mime_type = self.file.file.content_type

        super().save(*args, **kwargs)

    def __str__(self):
        return self.filename
