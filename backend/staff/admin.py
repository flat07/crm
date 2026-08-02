from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Department, Permission, Role, User

# --- Model Admin Registrations ---


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "description")
    search_fields = ("code", "name")


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Setup layout options for lists
    list_display = (
        "email",
        "first_name",
        "last_name",
        "job_title",
        "department",
        "is_staff",
    )
    list_filter = ("is_staff", "department")
    search_fields = ("email", "first_name", "last_name", "job_title")
    ordering = ("first_name", "last_name")

    # Required structure override when extending BaseUserAdmin with custom fields
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "phone", "avatar")}),
        ("Work Info", {"fields": ("job_title", "department")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                )
            },
        ),
        ("Important Dates", {"fields": ("last_login",)}),
    )

    # Overriding fields for user creation form in admin if needed
    add_fieldsets = (
        (
            None,
            {
                "classes": ("collapse",),
                "fields": ("email", "password", "first_name", "last_name", "is_staff"),
            },
        ),
    )

    # Optimization queries to avoid N+1 issues in the list view
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related("department").prefetch_related("roles")
