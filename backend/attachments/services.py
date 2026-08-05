# backend/attachments/services.py
from django.db import transaction

from attachments.models import Attachment


@transaction.atomic
def create_attachment(*, user, **data):
    return Attachment.objects.create(
        uploaded_by=user,
        **data,
    )


@transaction.atomic
def update_attachment(*, attachment: Attachment, **data):
    for field, value in data.items():
        setattr(attachment, field, value)

    attachment.save()

    return attachment


@transaction.atomic
def archive(*, attachment: Attachment) -> Attachment:
    attachment.soft_delete()
    return attachment


@transaction.atomic
def restore(*, attachment: Attachment) -> Attachment:
    attachment.restore()
    return attachment


@transaction.atomic
def delete_attachment(*, attachment: Attachment):
    attachment.delete()
