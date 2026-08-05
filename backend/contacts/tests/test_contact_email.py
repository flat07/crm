# backend/contacts/tests/test_contact_email.py

import pytest
from rest_framework import status

from contacts.models import ContactEmail
from contacts.tests.factories import (
    ContactEmailFactory,
    ContactFactory,
)

pytestmark = pytest.mark.django_db


class TestContactEmailList:
    endpoint = "/api/v1/contacts/email/"

    def test_returns_contact_email_list(
        self,
        auth_admin,
    ):
        ContactEmailFactory.create_batch(3)

        response = auth_admin.get(self.endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 3


class TestContactEmailRetrieve:
    endpoint = "/api/v1/contacts/email/{id}/"

    def test_returns_contact_email_detail(
        self,
        auth_admin,
    ):
        email = ContactEmailFactory()

        response = auth_admin.get(
            self.endpoint.format(id=email.id),
        )

        assert response.status_code == status.HTTP_200_OK
        print("DEBUG: response.data ", response.data)
        assert response.data["id"] == str(email.id)
        assert response.data["email"] == email.email

    def test_returns_404_for_unknown_contact_email(
        self,
        auth_admin,
    ):
        response = auth_admin.get(
            self.endpoint.format(
                id="00000000-0000-0000-0000-000000000000",
            ),
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND


class TestContactEmailCreate:
    endpoint = "/api/v1/contacts/email/"

    def test_creates_contact_email(
        self,
        auth_admin,
    ):
        contact = ContactFactory()

        payload = {
            "contact": str(contact.id),
            "email": "john@example.com",
            "is_primary": True,
        }

        response = auth_admin.post(
            self.endpoint,
            payload,
            format="json",
        )

        assert response.status_code == status.HTTP_201_CREATED

        assert ContactEmail.objects.filter(
            email="john@example.com",
        ).exists()

    def test_requires_contact(
        self,
        auth_admin,
    ):
        response = auth_admin.post(
            self.endpoint,
            {
                "email": "john@example.com",
            },
            format="json",
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "contact" in response.data

    def test_requires_email(
        self,
        auth_admin,
    ):
        contact = ContactFactory()

        response = auth_admin.post(
            self.endpoint,
            {
                "contact": str(contact.id),
            },
            format="json",
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "email" in response.data


class TestContactEmailUpdate:
    def test_updates_contact_email(
        self,
        auth_admin,
    ):
        contact_email = ContactEmailFactory(
            email="old@example.com",
        )

        response = auth_admin.patch(
            f"/api/v1/contacts/email/{contact_email.id}/",
            {
                "email": "new@example.com",
                "is_primary": True,
            },
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK

        contact_email.refresh_from_db()

        assert contact_email.email == "new@example.com"
        assert contact_email.is_primary is True


class TestContactEmailDelete:
    endpoint = "/api/v1/contacts/email/{id}/"

    def test_soft_deletes_contact_email(
        self,
        auth_admin,
    ):
        contact_email = ContactEmailFactory()

        response = auth_admin.delete(
            self.endpoint.format(id=contact_email.id),
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT

        contact_email.refresh_from_db()

        assert contact_email.deleted_at is not None
        assert contact_email.is_deleted is True


class TestContactEmailRestore:
    endpoint = "/api/v1/contacts/email/{id}/restore/"

    def test_restores_contact_email(
        self,
        auth_admin,
    ):
        contact_email = ContactEmailFactory()

        contact_email.soft_delete()

        response = auth_admin.post(
            self.endpoint.format(id=contact_email.id),
        )

        assert response.status_code == status.HTTP_200_OK

        contact_email.refresh_from_db()

        assert contact_email.deleted_at is None
        assert contact_email.is_deleted is False


class TestContactEmailHardDelete:
    endpoint = "/api/v1/contacts/email/{id}/hard_delete/"

    def test_hard_deletes_contact_email(
        self,
        auth_admin,
    ):
        contact_email = ContactEmailFactory()

        response = auth_admin.delete(
            self.endpoint.format(id=contact_email.id),
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT

        assert not ContactEmail.objects.filter(
            id=contact_email.id,
        ).exists()
