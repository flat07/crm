from django.contrib import admin

from .models import Attachment


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = (
        "filename",
        "uploaded_by",
        "file_size",
        "created_at",
    )

    search_fields = ("filename",)

    readonly_fields = (
        "file_size",
        "mime_type",
    )
