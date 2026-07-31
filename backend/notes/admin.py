from django.contrib import admin

from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "created_by",
        "is_pinned",
        "is_private",
        "created_at",
    )

    list_filter = (
        "is_pinned",
        "is_private",
    )

    search_fields = (
        "title",
        "content",
    )
