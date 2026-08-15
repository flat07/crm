# backend/notes/filters.py - Extended version

from django.db import models
from django_filters import rest_framework as filters

from .models import Note


class NoteFilter(filters.FilterSet):
    # Date filters
    created_at_after = filters.DateFilter(
        field_name="created_at",
        lookup_expr="date__gte",
    )

    created_at_before = filters.DateFilter(
        field_name="created_at",
        lookup_expr="date__lte",
    )

    created_at_range = filters.DateFromToRangeFilter(
        field_name="created_at",
        label="Created at range",
    )

    updated_at_after = filters.DateFilter(
        field_name="updated_at",
        lookup_expr="date__gte",
    )

    updated_at_before = filters.DateFilter(
        field_name="updated_at",
        lookup_expr="date__lte",
    )

    # Boolean filters
    is_pinned = filters.BooleanFilter(
        field_name="is_pinned",
    )

    is_private = filters.BooleanFilter(
        field_name="is_private",
    )

    # Content type filter with choices
    content_type = filters.ChoiceFilter(
        field_name="content_type__model",
        lookup_expr="iexact",
        choices=[
            ("company", "Company"),
            ("contact", "Contact"),
            ("lead", "Lead"),
            ("deal", "Deal"),
        ],
    )

    # Object ID filter
    object_id = filters.CharFilter(
        field_name="object_id",
    )

    # Created by filter
    created_by = filters.UUIDFilter(
        field_name="created_by__id",
    )

    created_by_name = filters.CharFilter(
        field_name="created_by__get_full_name",
        lookup_expr="icontains",
        label="Created by name contains",
    )

    # Combined content filter (title OR content)
    text = filters.CharFilter(
        method="filter_text",
        label="Search in title and content",
    )

    # Filter for notes linked to a specific object
    object = filters.CharFilter(
        method="filter_object",
        label="Object (content_type:object_id)",
    )

    def filter_text(self, queryset, name, value):
        """Search in both title and content."""
        if not value:
            return queryset

        return queryset.filter(
            models.Q(title__icontains=value) | models.Q(content__icontains=value)
        )

    def filter_object(self, queryset, name, value):
        """Filter by object in format 'content_type:object_id'."""
        if not value or ":" not in value:
            return queryset

        content_type, object_id = value.split(":", 1)

        return queryset.filter(
            content_type__model__iexact=content_type,
            object_id=object_id,
        )

    class Meta:
        model = Note
        fields = (
            "content_type",
            "object_id",
            "created_by",
            "is_pinned",
            "is_private",
        )
        # fields = {
        #     "content_type": ["exact", "in"],
        #     "object_id": ["exact", "in"],
        #     "created_by": ["exact", "in"],
        #     "is_pinned": ["exact"],
        #     "is_private": ["exact"],
        # }

    # You can also define filters explicitly like above
    # or use the Meta fields with lookup expressions
