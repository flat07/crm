from __future__ import annotations

from common.models import BaseModel
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class ActivityType(models.TextChoices):
    CALL = "call", "Call"
    EMAIL = "email", "Email"
    MEETING = "meeting", "Meeting"
    TASK = "task", "Task"
    NOTE = "note", "Note"


class ActivityStatus(models.TextChoices):
    PLANNED = "planned", "Planned"
    IN_PROGRESS = "in_progress", "In Progress"
    COMPLETED = "completed", "Completed"
    CANCELLED = "cancelled", "Cancelled"


class ActivityPriority(models.TextChoices):
    LOW = "low", "Low"
    MEDIUM = "medium", "Medium"
    HIGH = "high", "High"
    URGENT = "urgent", "Urgent"


class Activity(BaseModel):
    title = models.CharField(
        max_length=255,
    )

    description = models.TextField(
        blank=True,
    )

    activity_type = models.CharField(
        max_length=20,
        choices=ActivityType.choices,
        db_index=True,
    )

    status = models.CharField(
        max_length=20,
        choices=ActivityStatus.choices,
        default=ActivityStatus.PLANNED,
        db_index=True,
    )

    priority = models.CharField(
        max_length=20,
        choices=ActivityPriority.choices,
        default=ActivityPriority.MEDIUM,
    )

    due_date = models.DateTimeField(
        null=True,
        blank=True,
    )

    completed_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    owner = models.ForeignKey(
        "staff.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="owned_activities",
    )

    created_by = models.ForeignKey(
        "staff.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="created_activities",
    )

    # Generic relation
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
        ordering = ("-due_date", "-created_at")

        indexes = (
            models.Index(fields=["activity_type"]),
            models.Index(fields=["status"]),
            models.Index(fields=["owner"]),
            models.Index(fields=["content_type", "object_id"]),
        )

    def __str__(self):
        return self.title
