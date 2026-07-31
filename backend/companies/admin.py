from django.contrib import admin

from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "industry",
        "company_type",
        "owner",
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "phone",
    )

    list_filter = (
        "industry",
        "company_type",
        "is_active",
    )
