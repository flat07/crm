# backend/companies/api/filters.py

from django_filters import rest_framework as filters

from companies.models import Company


class CompanyFilter(filters.FilterSet):
    class Meta:
        model = Company

        fields = {  # noqa: RUF012
            "industry": ["exact"],
            "company_type": ["exact"],
            "size": ["exact"],
            "owner": ["exact"],
            "country": ["exact"],
            "city": ["exact"],
            "is_active": ["exact"],
        }
