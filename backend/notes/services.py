# backend/notes/services.py

from django.contrib.contenttypes.models import ContentType
from django.db import transaction

from .models import Note

CONTENT_TYPE_MAP = {
    "company": "companies.company",
    "contact": "contacts.contact",
    "lead": "leads.lead",
    "deal": "deals.deal",
}


@transaction.atomic
def create_note(
    *,
    title="",
    content,
    created_by,
    content_type,
    object_id,
    is_pinned=False,
    is_private=False,
) -> Note:
    app_label, model = CONTENT_TYPE_MAP[content_type].split(".")

    content_type_obj = ContentType.objects.get(
        app_label=app_label,
        model=model,
    )

    return Note.objects.create(
        title=title,
        content=content,
        created_by=created_by,
        is_pinned=is_pinned,
        is_private=is_private,
        content_type=content_type_obj,
        object_id=object_id,
    )


@transaction.atomic
def update_note(
    *,
    note,
    title=None,
    content=None,
    is_pinned=None,
    is_private=None,
    content_object=None,
) -> Note:

    if title is not None:
        note.title = title

    if content is not None:
        note.content = content

    if is_pinned is not None:
        note.is_pinned = is_pinned

    if is_private is not None:
        note.is_private = is_private

    if content_object is not None:
        note.content_type = ContentType.objects.get_for_model(
            content_object,
        )
        note.object_id = content_object.pk

    note.save()

    return note


@transaction.atomic
def archive(*, note: Note) -> Note:
    note.soft_delete()
    return note


@transaction.atomic
def restore(*, note: Note) -> Note:
    note.restore()
    return note


@transaction.atomic
def delete_note(
    *,
    note,
) -> None:
    note.delete()


@transaction.atomic
def pin_note(
    *,
    note,
) -> Note:

    note.is_pinned = True
    note.save(update_fields=["is_pinned"])

    return note


@transaction.atomic
def unpin_note(
    *,
    note,
) -> Note:

    note.is_pinned = False
    note.save(update_fields=["is_pinned"])

    return note


@transaction.atomic
def toggle_pin(
    *,
    note,
) -> Note:

    note.is_pinned = not note.is_pinned
    note.save(update_fields=["is_pinned"])

    return note


@transaction.atomic
def toggle_private(
    *,
    note,
) -> Note:

    note.is_private = not note.is_private
    note.save(update_fields=["is_private"])

    return note
