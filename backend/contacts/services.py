# backend/contacts/services.py

from django.db import transaction

from .models import Contact


@transaction.atomic
def create_contact(**validated_data) -> Contact:
    return Contact.objects.create(**validated_data)


@transaction.atomic
def update_contact(
    *,
    contact: Contact,
    **validated_data,
) -> Contact:
    for field, value in validated_data.items():
        setattr(contact, field, value)

    contact.save()

    return contact


@transaction.atomic
def archive(*, contact: Contact) -> Contact:
    contact.soft_delete()
    return contact


@transaction.atomic
def restore(*, contact: Contact) -> Contact:
    contact.restore()
    return contact


@transaction.atomic
def delete_contact(contact: Contact) -> None:
    contact.delete()
