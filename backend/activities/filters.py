# backend/activities/filters.py

from django_filters import rest_framework as filters

from .models import Activity


class ActivityFilter(filters.FilterSet):
    created_at_after = filters.DateFilter(
        field_name="created_at",
        lookup_expr="date__gte",
    )

    created_at_before = filters.DateFilter(
        field_name="created_at",
        lookup_expr="date__lte",
    )

    due_after = filters.DateTimeFilter(
        field_name="due_date",
        lookup_expr="gte",
    )

    due_before = filters.DateTimeFilter(
        field_name="due_date",
        lookup_expr="lte",
    )

    completed_after = filters.DateTimeFilter(
        field_name="completed_at",
        lookup_expr="gte",
    )

    completed_before = filters.DateTimeFilter(
        field_name="completed_at",
        lookup_expr="lte",
    )
    content_type = filters.CharFilter(
        field_name="content_type__model",
        lookup_expr="iexact",
    )

    object_id = filters.UUIDFilter(
        field_name="object_id",
    )

    class Meta:
        model = Activity

        fields = (
            "activity_type",
            "status",
            "priority",
            "owner",
            "created_by",
            "content_type",
            "object_id",
            "is_active",
        )
