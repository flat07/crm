# backend/contacts/tests/test_contact_email_filters.py

import pytest
from rest_framework import status

from contacts.tests.factories import (
    ContactEmailFactory,
    ContactFactory,
)

pytestmark = pytest.mark.django_db


class TestContactEmailFilterContact:
    endpoint = "/api/v1/contacts/email/"

    def test_filters_by_contact(
        self,
        auth_admin,
    ):
        contact1 = ContactFactory()
        contact2 = ContactFactory()

        ContactEmailFactory(
            contact=contact1,
            email="john@example.com",
        )

        ContactEmailFactory(
            contact=contact2,
            email="jane@example.com",
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "contact": str(contact1.id),
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["contact"] == contact1.id


class TestContactEmailFilterEmailExact:
    endpoint = "/api/v1/contacts/email/"

    def test_filters_by_exact_email(
        self,
        auth_admin,
    ):
        ContactEmailFactory(email="john@example.com")
        ContactEmailFactory(email="jane@example.com")

        response = auth_admin.get(
            self.endpoint,
            {
                "email": "john@example.com",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["email"] == "john@example.com"


class TestContactEmailFilterEmailContains:
    endpoint = "/api/v1/contacts/email/"

    def test_filters_by_email_icontains(
        self,
        auth_admin,
    ):
        ContactEmailFactory(email="john@example.com")
        ContactEmailFactory(email="jane@example.com")
        ContactEmailFactory(email="john.smith@gmail.com")

        response = auth_admin.get(
            self.endpoint,
            {
                "email__icontains": "john",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2

        emails = {item["email"] for item in response.data}

        assert emails == {
            "john@example.com",
            "john.smith@gmail.com",
        }


class TestContactEmailFilterPrimary:
    endpoint = "/api/v1/contacts/email/"

    def test_filters_primary_emails(
        self,
        auth_admin,
    ):
        ContactEmailFactory(
            email="primary@example.com",
            is_primary=True,
        )

        ContactEmailFactory(
            email="secondary@example.com",
            is_primary=False,
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "is_primary": True,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["email"] == "primary@example.com"

    def test_filters_non_primary_emails(
        self,
        auth_admin,
    ):
        ContactEmailFactory(
            email="primary@example.com",
            is_primary=True,
        )

        ContactEmailFactory(
            email="secondary@example.com",
            is_primary=False,
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "is_primary": False,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["email"] == "secondary@example.com"


class TestContactEmailSearch:
    endpoint = "/api/v1/contacts/email/"

    def test_search_email(
        self,
        auth_admin,
    ):
        ContactEmailFactory(
            email="john@example.com",
        )

        ContactEmailFactory(
            email="jane@example.com",
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "search": "john",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["email"] == "john@example.com"

    def test_search_contact_first_name(
        self,
        auth_admin,
    ):
        john = ContactFactory(
            first_name="John",
            last_name="Smith",
        )

        jane = ContactFactory(
            first_name="Jane",
            last_name="Doe",
        )

        ContactEmailFactory(
            contact=john,
            email="john@example.com",
        )

        ContactEmailFactory(
            contact=jane,
            email="jane@example.com",
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "search": "John",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["contact"] == john.id

    def test_search_returns_empty(
        self,
        auth_admin,
    ):
        ContactEmailFactory()

        response = auth_admin.get(
            self.endpoint,
            {
                "search": "xxxxxxxx",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data == []


class TestContactEmailOrdering:
    endpoint = "/api/v1/contacts/email/"

    def test_orders_email_ascending(
        self,
        auth_admin,
    ):
        ContactEmailFactory(
            email="z@example.com",
        )

        ContactEmailFactory(
            email="a@example.com",
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "ordering": "email",
            },
        )

        assert response.status_code == status.HTTP_200_OK

        emails = [item["email"] for item in response.data]

        assert emails == sorted(emails)

    def test_orders_email_descending(
        self,
        auth_admin,
    ):
        ContactEmailFactory(
            email="a@example.com",
        )

        ContactEmailFactory(
            email="z@example.com",
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "ordering": "-email",
            },
        )

        assert response.status_code == status.HTTP_200_OK

        emails = [item["email"] for item in response.data]

        assert emails == sorted(
            emails,
            reverse=True,
        )
