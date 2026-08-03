# backend/contacts/api/filters.py

from django_filters import rest_framework as filters

from contacts.models import Contact


class ContactFilter(filters.FilterSet):
    class Meta:
        model = Contact

        fields = {  # noqa: RUF012
            "first_name": ["exact"],
            "last_name": ["exact"],
            "job_title": ["exact"],
            "email": ["exact"],
            "phone": ["exact"],
            "mobile": ["exact"],
            "city": ["exact"],
            "country": ["exact"],
        }
