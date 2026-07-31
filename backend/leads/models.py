from __future__ import annotations

from decimal import Decimal

from common.models import BaseModel
from django.db import models


class LeadStatus(models.TextChoices):
    NEW = "new", "New"
    CONTACTED = "contacted", "Contacted"
    QUALIFIED = "qualified", "Qualified"
    PROPOSAL_SENT = "proposal_sent", "Proposal Sent"
    NEGOTIATION = "negotiation", "Negotiation"
    WON = "won", "Won"
    LOST = "lost", "Lost"


class LeadSource(models.TextChoices):
    WEBSITE = "website", "Website"
    REFERRAL = "referral", "Referral"
    COLD_CALL = "cold_call", "Cold Call"
    EMAIL = "email", "Email"
    SOCIAL_MEDIA = "social_media", "Social Media"
    EVENT = "event", "Event"
    OTHER = "other", "Other"


class Lead(BaseModel):
    title = models.CharField(
        max_length=255,
    )

    company = models.ForeignKey(
        "companies.Company",
        on_delete=models.CASCADE,
        related_name="leads",
    )

    contact = models.ForeignKey(
        "contacts.Contact",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="leads",
    )

    source = models.CharField(
        max_length=50,
        choices=LeadSource.choices,
        default=LeadSource.OTHER,
        db_index=True,
    )

    status = models.CharField(
        max_length=50,
        choices=LeadStatus.choices,
        default=LeadStatus.NEW,
        db_index=True,
    )

    estimated_value = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.00"),
    )

    probability = models.PositiveSmallIntegerField(
        default=0,
        help_text="0 - 100",
    )

    expected_close_date = models.DateField(
        null=True,
        blank=True,
    )

    owner = models.ForeignKey(
        "staff.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="owned_leads",
    )

    description = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ("-created_at",)

        indexes = (
            models.Index(fields=["status"]),
            models.Index(fields=["source"]),
            models.Index(fields=["owner"]),
        )

    def __str__(self):
        return self.title


class LeadStatusHistory(BaseModel):
    lead = models.ForeignKey(
        Lead,
        on_delete=models.CASCADE,
        related_name="status_history",
    )

    old_status = models.CharField(
        max_length=50,
        choices=LeadStatus.choices,
    )

    new_status = models.CharField(
        max_length=50,
        choices=LeadStatus.choices,
    )

    changed_by = models.ForeignKey(
        "staff.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="lead_status_changes",
    )

    notes = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.lead} {self.old_status} → {self.new_status}"


class LeadAssignment(BaseModel):
    lead = models.ForeignKey(
        Lead,
        on_delete=models.CASCADE,
        related_name="assignments",
    )

    assigned_to = models.ForeignKey(
        "staff.User",
        on_delete=models.CASCADE,
        related_name="lead_assignments",
    )

    assigned_by = models.ForeignKey(
        "staff.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="assigned_leads",
    )

    assigned_at = models.DateTimeField(
        auto_now_add=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = ("-assigned_at",)

    def __str__(self):
        return f"{self.lead} -> {self.assigned_to}"
