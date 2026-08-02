# backend/companies/selectors.py

from django.db.models import QuerySet

from .models import Company


def company_list(*, include_deleted: bool = False) -> QuerySet[Company]:
    queryset = Company.objects.select_related(
        "owner",
        "created_by",
    )

    if not include_deleted:
        queryset = queryset.filter(deleted_at__isnull=True)

    return queryset


def company_detail(*, company_id) -> Company:
    return (
        Company.objects.select_related(
            "owner",
            "created_by",
        )
        .filter(
            deleted_at__isnull=True,
        )
        .get(id=company_id)
    )
