from django.contrib import admin

from .models import (
    Lead,
    LeadAssignment,
    LeadStatusHistory,
)


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "company",
        "status",
        "estimated_value",
        "owner",
        "created_at",
    )

    list_filter = (
        "status",
        "source",
    )

    search_fields = (
        "title",
        "company__name",
    )


@admin.register(LeadStatusHistory)
class LeadStatusHistoryAdmin(admin.ModelAdmin):
    list_display = (
        "lead",
        "old_status",
        "new_status",
        "changed_by",
        "created_at",
    )


@admin.register(LeadAssignment)
class LeadAssignmentAdmin(admin.ModelAdmin):
    list_display = (
        "lead",
        "assigned_to",
        "assigned_by",
        "assigned_at",
        "is_active",
    )
