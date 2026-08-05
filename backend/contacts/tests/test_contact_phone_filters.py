# backend/contacts/tests/test_contact_phone_filters.py

import pytest
from rest_framework import status

from contacts.tests.factories import (
    ContactFactory,
    ContactPhoneFactory,
)

pytestmark = pytest.mark.django_db


class TestContactPhoneFilterContact:
    endpoint = "/api/v1/contacts/phone/"

    def test_filters_by_contact(
        self,
        auth_admin,
    ):
        contact1 = ContactFactory()
        contact2 = ContactFactory()

        ContactPhoneFactory(
            contact=contact1,
            phone="+15550000001",
        )

        ContactPhoneFactory(
            contact=contact2,
            phone="+15550000002",
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "contact": str(contact1.id),
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["contact"] == contact1.id


class TestContactPhoneFilterPhoneExact:
    endpoint = "/api/v1/contacts/phone/"

    def test_filters_by_exact_phone(
        self,
        auth_admin,
    ):
        ContactPhoneFactory(phone="+15550000001")
        ContactPhoneFactory(phone="+15550000002")

        response = auth_admin.get(
            self.endpoint,
            {
                "phone": "+15550000001",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["phone"] == "+15550000001"


class TestContactPhoneFilterPhoneContains:
    endpoint = "/api/v1/contacts/phone/"

    def test_filters_by_phone_icontains(
        self,
        auth_admin,
    ):
        ContactPhoneFactory(phone="+998901112233")
        ContactPhoneFactory(phone="+998931234567")
        ContactPhoneFactory(phone="+441234567890")

        response = auth_admin.get(
            self.endpoint,
            {
                "phone__icontains": "998",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 2

        phones = {item["phone"] for item in response.data["results"]}

        assert phones == {
            "+998901112233",
            "+998931234567",
        }


class TestContactPhoneFilterPrimary:
    endpoint = "/api/v1/contacts/phone/"

    def test_filters_primary_phones(
        self,
        auth_admin,
    ):
        ContactPhoneFactory(
            phone="+15550000001",
            is_primary=True,
        )

        ContactPhoneFactory(
            phone="+15550000002",
            is_primary=False,
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "is_primary": True,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["phone"] == "+15550000001"

    def test_filters_non_primary_phones(
        self,
        auth_admin,
    ):
        ContactPhoneFactory(
            phone="+15550000001",
            is_primary=True,
        )

        ContactPhoneFactory(
            phone="+15550000002",
            is_primary=False,
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "is_primary": False,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["phone"] == "+15550000002"
