# backend/deals/api/filters.py

from django_filters import rest_framework as filters

from deals.models import Deal


class DealFilter(filters.FilterSet):
    class Meta:
        model = Deal

        fields = {  # noqa: RUF012
            "lead": ["exact"],
            "company__name": ["exact"],
            "contact__first_name": ["exact"],
            "contact__last_name": ["exact"],
            "owner": ["exact"],
            "is_active": ["exact"],
            "created_at": ["exact"],
            "updated_at": ["exact"],
        }
