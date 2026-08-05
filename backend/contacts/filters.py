# backend/contacts/api/filters.py

from django_filters import rest_framework as filters

from .models import (
    Contact,
    ContactEmail,
    ContactPhone,
    ContactTag,
    ContactTagAssignment,
)


class ContactFilter(filters.FilterSet):
    created_at_after = filters.DateFilter(
        field_name="created_at",
        lookup_expr="date__gte",
    )

    created_at_before = filters.DateFilter(
        field_name="created_at",
        lookup_expr="date__lte",
    )

    birthday_after = filters.DateFilter(
        field_name="birthday",
        lookup_expr="gte",
    )

    birthday_before = filters.DateFilter(
        field_name="birthday",
        lookup_expr="lte",
    )

    city = filters.CharFilter(
        field_name="city",
        lookup_expr="iexact",
    )

    country = filters.CharFilter(
        field_name="country",
        lookup_expr="iexact",
    )

    class Meta:
        model = Contact

        fields = (
            "contact_type",
            "source",
            "company",
            "owner",
            "is_active",
        )


class ContactTagFilter(filters.FilterSet):
    class Meta:
        model = ContactTag
        fields = {  # noqa: RUF012
            "name": ["exact", "icontains"],
        }


class ContactEmailFilter(filters.FilterSet):
    class Meta:
        model = ContactEmail
        fields = {  # noqa: RUF012
            "contact": ["exact"],
            "email": ["exact", "icontains"],
            "is_primary": ["exact"],
        }


class ContactPhoneFilter(filters.FilterSet):
    class Meta:
        model = ContactPhone
        fields = {  # noqa: RUF012
            "contact": ["exact"],
            "phone": ["exact", "icontains"],
            "is_primary": ["exact"],
        }


class ContactTagAssignmentFilter(filters.FilterSet):
    class Meta:
        model = ContactTagAssignment
        fields = {  # noqa: RUF012
            "contact": ["exact"],
            "tag": ["exact"],
        }
