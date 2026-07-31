# backend/common/choices.py

from django.db import models


class PhoneType(models.TextChoices):
    MOBILE = "mobile", "Mobile"
    HOME = "home", "Home"
    WORK = "work", "Work"
    OTHER = "other", "Other"


class AddressType(models.TextChoices):
    BILLING = "billing", "Billing"
    SHIPPING = "shipping", "Shipping"
    OFFICE = "office", "Office"
    HOME = "home", "Home"


class ActivityStatus(models.TextChoices):
    PENDING = "pending", "Pending"
    IN_PROGRESS = "in_progress", "In Progress"
    COMPLETED = "completed", "Completed"
    CANCELLED = "cancelled", "Cancelled"


class Priority(models.TextChoices):
    LOW = "low", "Low"
    MEDIUM = "medium", "Medium"
    HIGH = "high", "High"
    URGENT = "urgent", "Urgent"
