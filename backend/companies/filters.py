# backend/companies/filters.py

from django_filters import rest_framework as filters

from .models import Company


class CompanyFilter(filters.FilterSet):
    name = filters.CharFilter(
        lookup_expr="icontains",
    )

    legal_name = filters.CharFilter(
        lookup_expr="icontains",
    )

    city = filters.CharFilter(
        lookup_expr="icontains",
    )

    country = filters.CharFilter(
        lookup_expr="icontains",
    )

    email = filters.CharFilter(
        lookup_expr="icontains",
    )

    owner = filters.UUIDFilter(
        field_name="owner_id",
    )

    created_by = filters.UUIDFilter(
        field_name="created_by_id",
    )

    created_after = filters.DateTimeFilter(
        field_name="created_at",
        lookup_expr="gte",
    )

    created_before = filters.DateTimeFilter(
        field_name="created_at",
        lookup_expr="lte",
    )

    class Meta:
        model = Company

        fields = (
            "industry",
            "company_type",
            "size",
            "is_active",
            "owner",
            "created_by",
            "city",
            "country",
            "name",
            "legal_name",
            "email",
        )
