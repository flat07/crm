# backend/deals/selectors.py

from django.db.models import Prefetch, QuerySet

from .models import (
    Deal,
    DealCompetitor,
    DealProduct,
    DealStageHistory,
)


def deal_list() -> QuerySet[Deal]:
    return Deal.objects.select_related(
        "lead",
        "company",
        "contact",
        "owner",
    ).prefetch_related(
        Prefetch(
            "products",
            queryset=DealProduct.objects.order_by("name"),
        ),
        Prefetch(
            "competitors",
            queryset=DealCompetitor.objects.order_by("name"),
        ),
        Prefetch(
            "stage_history",
            queryset=DealStageHistory.objects.select_related(
                "changed_by",
            ),
        ),
    )


def deal_detail(deal_id):
    return deal_list().get(pk=deal_id)
