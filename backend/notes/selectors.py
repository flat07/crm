# backend/notes/selectors.py

from django.contrib.contenttypes.models import ContentType
from django.db.models import QuerySet

from .models import Note


def note_list() -> QuerySet[Note]:
    return (
        Note.objects.filter(deleted_at__isnull=True)
        .select_related(
            "created_by",
            "content_type",
        )
        .all()
    )


def note_detail(pk) -> Note:
    return Note.objects.select_related(
        "created_by",
        "content_type",
    ).get(pk=pk)


def notes_for_object(
    *,
    content_object,
) -> QuerySet[Note]:
    content_type = ContentType.objects.get_for_model(
        content_object,
    )

    return note_list().filter(
        content_type=content_type,
        object_id=content_object.pk,
    )


def note_detail_with_deleted(note_id) -> Note:
    return Note.objects.select_related(
        "created_by",
        "content_type",
    ).get(pk=note_id)


def notes_for_user(
    *,
    user,
) -> QuerySet[Note]:
    return note_list().filter(created_by=user)


def pinned_notes() -> QuerySet[Note]:
    return note_list().filter(is_pinned=True)


def private_notes() -> QuerySet[Note]:
    return note_list().filter(is_private=True)
