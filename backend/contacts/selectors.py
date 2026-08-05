# backend/contacts/selectors.py

from django.db.models import Prefetch, QuerySet

from .models import (
    Contact,
    ContactEmail,
    ContactPhone,
    ContactTag,
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


def contact_tag_list():
    return ContactTag.objects.all()


def contact_tag_detail(pk: int):
    return ContactTag.objects.get(pk=pk)


def contact_email_list():
    return ContactEmail.objects.select_related("contact")


def contact_email_detail(pk: int):
    return ContactEmail.objects.select_related("contact").get(pk=pk)


def contact_phone_list():
    return ContactPhone.objects.select_related("contact")


def contact_phone_detail(pk: int):
    return ContactPhone.objects.select_related("contact").get(pk=pk)


def contact_assignment_list():
    return ContactTagAssignment.objects.select_related(
        "contact",
        "tag",
    )


def contact_assignment_detail(pk: int):
    return ContactTagAssignment.objects.select_related(
        "contact",
        "tag",
    ).get(pk=pk)
