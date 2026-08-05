# backend/attachments/selectors.py

from attachments.models import Attachment


def attachment_list():
    return Attachment.objects.select_related(
        "uploaded_by",
        "content_type",
    )


def attachment_detail(*, pk):
    return Attachment.objects.select_related(
        "uploaded_by",
        "content_type",
    ).get(pk=pk)
