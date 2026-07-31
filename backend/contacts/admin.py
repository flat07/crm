from django.contrib import admin

# Register your models here.
from .models import (
    Contact,
    ContactEmail,
    ContactPhone,
    ContactTag,
)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "company",
        "email",
        "owner",
        "contact_type",
        "is_active",
    )

    search_fields = (
        "first_name",
        "last_name",
        "email",
        "company__name",
    )

    list_filter = (
        "contact_type",
        "source",
        "is_active",
    )


@admin.register(ContactEmail)
class ContactEmailAdmin(admin.ModelAdmin):
    list_display = (
        "contact",
        "email",
        "is_primary",
    )


@admin.register(ContactPhone)
class ContactPhoneAdmin(admin.ModelAdmin):
    list_display = (
        "contact",
        "phone",
        "is_primary",
    )


@admin.register(ContactTag)
class ContactTagAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "is_active",
    )
