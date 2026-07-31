from __future__ import annotations

from common.models import BaseModel
from django.db import models


class DealStage(models.TextChoices):
    PROSPECTING = "prospecting", "Prospecting"
    DISCOVERY = "discovery", "Discovery"
    PROPOSAL = "proposal", "Proposal"
    NEGOTIATION = "negotiation", "Negotiation"
    CONTRACT = "contract", "Contract"
    WON = "won", "Won"
    LOST = "lost", "Lost"


class Deal(BaseModel):
    lead = models.OneToOneField(
        "leads.Lead",
        on_delete=models.CASCADE,
        related_name="deal",
    )

    company = models.ForeignKey(
        "companies.Company",
        on_delete=models.CASCADE,
        related_name="deals",
    )

    contact = models.ForeignKey(
        "contacts.Contact",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="deals",
    )

    owner = models.ForeignKey(
        "staff.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="owned_deals",
    )

    stage = models.CharField(
        max_length=50,
        choices=DealStage.choices,
        default=DealStage.PROSPECTING,
        db_index=True,
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    probability = models.PositiveSmallIntegerField(
        default=0,
    )

    expected_close_date = models.DateField(
        null=True,
        blank=True,
    )

    actual_close_date = models.DateField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ("-created_at",)

        indexes = (
            models.Index(fields=["stage"]),
            models.Index(fields=["owner"]),
            models.Index(fields=["expected_close_date"]),
        )

    def __str__(self):
        return f"{self.company} - {self.amount}"


class DealStageHistory(BaseModel):
    deal = models.ForeignKey(
        Deal,
        on_delete=models.CASCADE,
        related_name="stage_history",
    )

    old_stage = models.CharField(
        max_length=50,
        choices=DealStage.choices,
    )

    new_stage = models.CharField(
        max_length=50,
        choices=DealStage.choices,
    )

    changed_by = models.ForeignKey(
        "staff.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="deal_stage_changes",
    )

    notes = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.deal} {self.old_stage} → {self.new_stage}"


class DealCompetitor(BaseModel):
    deal = models.ForeignKey(
        Deal,
        on_delete=models.CASCADE,
        related_name="competitors",
    )

    name = models.CharField(
        max_length=255,
    )

    notes = models.TextField(
        blank=True,
    )

    def __str__(self):
        return self.name


class DealProduct(BaseModel):
    deal = models.ForeignKey(
        Deal,
        on_delete=models.CASCADE,
        related_name="products",
    )

    name = models.CharField(
        max_length=255,
    )

    quantity = models.PositiveIntegerField(
        default=1,
    )

    unit_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    class Meta:
        ordering = ("name",)

    @property
    def total(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return self.name
