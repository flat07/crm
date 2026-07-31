from __future__ import annotations

from common.models import BaseModel
from django.db import models


class ContactType(models.TextChoices):
    CUSTOMER = "customer", "Customer"
    LEAD = "lead", "Lead"
    PARTNER = "partner", "Partner"
    VENDOR = "vendor", "Vendor"


class ContactSource(models.TextChoices):
    WEBSITE = "website", "Website"
    REFERRAL = "referral", "Referral"
    SOCIAL_MEDIA = "social_media", "Social Media"
    COLD_CALL = "cold_call", "Cold Call"
    EVENT = "event", "Event"
    OTHER = "other", "Other"


class Contact(BaseModel):
    first_name = models.CharField(
        max_length=100,
        db_index=True,
    )

    last_name = models.CharField(
        max_length=100,
        db_index=True,
    )

    job_title = models.CharField(
        max_length=150,
        blank=True,
    )

    email = models.EmailField(
        blank=True,
    )

    phone = models.CharField(
        max_length=30,
        blank=True,
    )

    mobile = models.CharField(
        max_length=30,
        blank=True,
    )

    contact_type = models.CharField(
        max_length=50,
        choices=ContactType.choices,
        default=ContactType.CUSTOMER,
        db_index=True,
    )

    source = models.CharField(
        max_length=50,
        choices=ContactSource.choices,
        default=ContactSource.OTHER,
        db_index=True,
    )

    company = models.ForeignKey(
        "companies.Company",
        on_delete=models.CASCADE,
        related_name="contacts",
    )

    owner = models.ForeignKey(
        "staff.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="owned_contacts",
    )

    notes = models.TextField(
        blank=True,
    )

    birthday = models.DateField(
        null=True,
        blank=True,
    )

    linkedin_url = models.URLField(
        max_length=500,
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

    class Meta:
        ordering = (
            "first_name",
            "last_name",
        )
        indexes = (
            models.Index(fields=["first_name", "last_name"]),
            models.Index(fields=["email"]),
            models.Index(fields=["contact_type"]),
        )

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return (f"{self.first_name} {self.last_name}").strip()


class ContactTag(BaseModel):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class ContactTagAssignment(BaseModel):
    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        related_name="tag_assignments",
    )

    tag = models.ForeignKey(
        ContactTag,
        on_delete=models.CASCADE,
        related_name="contacts",
    )

    class Meta:
        unique_together = (
            "contact",
            "tag",
        )

    def __str__(self):
        return f"{self.contact} - {self.tag}"


class ContactEmail(BaseModel):
    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        related_name="emails",
    )

    email = models.EmailField()

    is_primary = models.BooleanField(
        default=False,
    )

    class Meta:
        ordering = ("-is_primary",)

    def __str__(self):
        return self.email


class ContactPhone(BaseModel):
    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        related_name="phones",
    )

    phone = models.CharField(
        max_length=30,
    )

    is_primary = models.BooleanField(
        default=False,
    )

    class Meta:
        ordering = ("-is_primary",)

    def __str__(self):
        return self.phone
