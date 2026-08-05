# backend/contacts/services.py

from django.db import transaction

from .models import (
    Contact,
    ContactEmail,
    ContactPhone,
    ContactTag,
    ContactTagAssignment,
)


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


@transaction.atomic
def create_contact_tag(**data):
    return ContactTag.objects.create(**data)


@transaction.atomic
def update_contact_tag(contact_tag: ContactTag, **data):
    for field, value in data.items():
        setattr(contact_tag, field, value)

    contact_tag.save()

    return contact_tag


@transaction.atomic
def archive_contact_tag(*, contact_tag: ContactTag) -> ContactTag:
    contact_tag.soft_delete()
    return contact_tag


@transaction.atomic
def restore_contact_tag(*, contact_tag: ContactTag) -> ContactTag:
    contact_tag.restore()
    return contact_tag


@transaction.atomic
def delete_contact_tag(contact_tag: ContactTag):
    contact_tag.delete()


def create_contact_email(**data):
    return ContactEmail.objects.create(**data)


def update_contact_email(instance: ContactEmail, **data):
    for field, value in data.items():
        setattr(instance, field, value)

    instance.save()

    return instance


@transaction.atomic
def archive_contact_email(*, instance: ContactEmail) -> ContactEmail:
    instance.soft_delete()
    return instance


@transaction.atomic
def restore_contact_email(*, instance: ContactEmail) -> ContactEmail:
    instance.restore()
    return instance


@transaction.atomic
def delete_contact_email(instance: ContactEmail):
    instance.delete()


@transaction.atomic
def create_contact_phone(**data):
    return ContactPhone.objects.create(**data)


@transaction.atomic
def update_contact_phone(instance: ContactPhone, **data):
    for field, value in data.items():
        setattr(instance, field, value)

    instance.save()

    return instance


@transaction.atomic
def archive_contact_phone(*, instance: ContactPhone) -> ContactPhone:
    instance.soft_delete()
    return instance


@transaction.atomic
def restore_contact_phone(*, instance: ContactPhone) -> ContactPhone:
    instance.restore()
    return instance


@transaction.atomic
def delete_contact_phone(instance: ContactPhone):
    instance.delete()


@transaction.atomic
def create_contact_assignment(**data):
    return ContactTagAssignment.objects.create(**data)


@transaction.atomic
def update_contact_assignment(instance: ContactTagAssignment, **data):
    for field, value in data.items():
        setattr(instance, field, value)

    instance.save()

    return instance


@transaction.atomic
def archive_contact_assignment(
    *, contact_assignment: ContactTagAssignment
) -> ContactTagAssignment:
    contact_assignment.soft_delete()
    return contact_assignment


@transaction.atomic
def restore_contact_assignment(
    *, contact_assignment: ContactTagAssignment
) -> ContactTagAssignment:
    contact_assignment.restore()
    return contact_assignment


@transaction.atomic
def delete_contact_assignment(instance: ContactTagAssignment):
    instance.delete()
