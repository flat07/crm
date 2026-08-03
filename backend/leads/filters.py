# backend/leads/filters.py

from django_filters import rest_framework as filters

from .models import Lead


class LeadFilter(filters.FilterSet):
    created_at_after = filters.DateFilter(
        field_name="created_at",
        lookup_expr="date__gte",
    )

    created_at_before = filters.DateFilter(
        field_name="created_at",
        lookup_expr="date__lte",
    )

    expected_close_after = filters.DateFilter(
        field_name="expected_close_date",
        lookup_expr="gte",
    )

    expected_close_before = filters.DateFilter(
        field_name="expected_close_date",
        lookup_expr="lte",
    )

    estimated_value_min = filters.NumberFilter(
        field_name="estimated_value",
        lookup_expr="gte",
    )

    estimated_value_max = filters.NumberFilter(
        field_name="estimated_value",
        lookup_expr="lte",
    )

    probability_min = filters.NumberFilter(
        field_name="probability",
        lookup_expr="gte",
    )

    probability_max = filters.NumberFilter(
        field_name="probability",
        lookup_expr="lte",
    )

    class Meta:
        model = Lead

        fields = (
            "status",
            "source",
            "company",
            "contact",
            "owner",
            "is_active",
        )
