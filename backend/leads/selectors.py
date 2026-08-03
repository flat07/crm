# backend/leads/selectors.py

from django.db.models import QuerySet

from .models import Lead


def lead_list() -> QuerySet[Lead]:
    return Lead.objects.select_related(
        "company",
        "contact",
        "owner",
    )


def lead_detail(lead_id) -> Lead:
    return lead_list().get(pk=lead_id)
