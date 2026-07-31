from __future__ import annotations

from common.models import BaseModel
from django.db import models


class Industry(models.TextChoices):
    TECHNOLOGY = "technology", "Technology"
    FINANCE = "finance", "Finance"
    HEALTHCARE = "healthcare", "Healthcare"
    EDUCATION = "education", "Education"
    HOSPITALITY = "hospitality", "Hospitality"
    RETAIL = "retail", "Retail"
    OTHER = "other", "Other"


class CompanySize(models.TextChoices):
    SMALL = "small", "Small"
    MEDIUM = "medium", "Medium"
    LARGE = "large", "Large"
    ENTERPRISE = "enterprise", "Enterprise"


class CompanyType(models.TextChoices):
    CUSTOMER = "customer", "Customer"
    PARTNER = "partner", "Partner"
    VENDOR = "vendor", "Vendor"
    PROSPECT = "prospect", "Prospect"


class Company(BaseModel):
    name = models.CharField(
        max_length=255,
        db_index=True,
    )

    legal_name = models.CharField(
        max_length=255,
        blank=True,
    )

    website = models.URLField(
        max_length=500,
        blank=True,
    )

    email = models.EmailField(
        blank=True,
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
    )

    industry = models.CharField(
        max_length=50,
        choices=Industry.choices,
        default=Industry.OTHER,
        db_index=True,
    )

    company_type = models.CharField(
        max_length=50,
        choices=CompanyType.choices,
        default=CompanyType.PROSPECT,
        db_index=True,
    )

    size = models.CharField(
        max_length=50,
        choices=CompanySize.choices,
        blank=True,
    )

    tax_number = models.CharField(
        max_length=100,
        blank=True,
    )

    description = models.TextField(
        blank=True,
    )

    address = models.TextField(
        blank=True,
    )

    city = models.CharField(
        max_length=100,
        blank=True,
    )

    country = models.CharField(
        max_length=100,
        blank=True,
    )

    postal_code = models.CharField(
        max_length=20,
        blank=True,
    )

    owner = models.ForeignKey(
        "staff.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="owned_companies",
    )

    created_by = models.ForeignKey(
        "staff.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="created_companies",
    )

    class Meta:
        ordering = ("name",)

        indexes = (
            models.Index(fields=["name"]),
            models.Index(fields=["industry"]),
            models.Index(fields=["company_type"]),
        )

    def __str__(self) -> str:
        return self.name
