# backend/contacts/selectors.py

from django.db.models import Prefetch, QuerySet

from .models import (
    Contact,
    ContactEmail,
    ContactPhone,
    ContactTagAssignment,
)


def contact_list() -> QuerySet[Contact]:
    return Contact.objects.select_related(
        "company",
        "owner",
    ).prefetch_related(
        Prefetch(
            "emails",
            queryset=ContactEmail.objects.order_by("-is_primary"),
        ),
        Prefetch(
            "phones",
            queryset=ContactPhone.objects.order_by("-is_primary"),
        ),
        Prefetch(
            "tag_assignments",
            queryset=ContactTagAssignment.objects.select_related("tag"),
        ),
    )


def contact_detail(contact_id: int) -> Contact:
    return contact_list().get(pk=contact_id)
