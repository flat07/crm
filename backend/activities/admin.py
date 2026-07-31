from django.contrib import admin

from .models import Activity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "activity_type",
        "status",
        "priority",
        "owner",
        "due_date",
    )

    list_filter = (
        "activity_type",
        "status",
        "priority",
    )

    search_fields = (
        "title",
        "description",
    )
