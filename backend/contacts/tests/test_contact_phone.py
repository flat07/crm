# backend/contacts/tests/test_contact_phone.py

import pytest
from rest_framework import status

from contacts.models import ContactPhone
from contacts.tests.factories import (
    ContactFactory,
    ContactPhoneFactory,
)

pytestmark = pytest.mark.django_db


class TestContactPhoneList:
    endpoint = "/api/v1/contacts/phone/"

    def test_returns_contact_phone_list(
        self,
        auth_admin,
    ):
        ContactPhoneFactory.create_batch(3)

        response = auth_admin.get(self.endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3


class TestContactPhoneRetrieve:
    endpoint = "/api/v1/contacts/phone/{id}/"

    def test_returns_contact_phone_detail(
        self,
        auth_admin,
    ):
        phone = ContactPhoneFactory()

        response = auth_admin.get(
            self.endpoint.format(id=phone.id),
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == str(phone.id)
        assert response.data["phone"] == phone.phone

    def test_returns_404_for_unknown_contact_phone(
        self,
        auth_admin,
    ):
        response = auth_admin.get(
            self.endpoint.format(
                id="00000000-0000-0000-0000-000000000000",
            ),
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND


class TestContactPhoneCreate:
    endpoint = "/api/v1/contacts/phone/"

    def test_creates_contact_phone(
        self,
        auth_admin,
    ):
        contact = ContactFactory()

        payload = {
            "contact": str(contact.id),
            "phone": "+15551234567",
            "is_primary": True,
        }

        response = auth_admin.post(
            self.endpoint,
            payload,
            format="json",
        )

        assert response.status_code == status.HTTP_201_CREATED

        assert ContactPhone.objects.filter(
            phone="+15551234567",
        ).exists()

    def test_requires_contact(
        self,
        auth_admin,
    ):
        response = auth_admin.post(
            self.endpoint,
            {
                "phone": "+15551234567",
            },
            format="json",
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "contact" in response.data

    def test_requires_phone(
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
        assert "phone" in response.data


class TestContactPhoneUpdate:
    endpoint = "/api/v1/contacts/phone/{id}/"

    def test_updates_contact_phone(
        self,
        auth_admin,
    ):
        contact_phone = ContactPhoneFactory(
            phone="+11111111111",
        )

        response = auth_admin.patch(
            self.endpoint.format(id=contact_phone.id),
            {
                "phone": "+22222222222",
                "is_primary": True,
            },
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK

        contact_phone.refresh_from_db()

        assert contact_phone.phone == "+22222222222"
        assert contact_phone.is_primary is True


class TestContactPhoneDelete:
    endpoint = "/api/v1/contacts/phone/{id}/"

    def test_soft_deletes_contact_phone(
        self,
        auth_admin,
    ):
        contact_phone = ContactPhoneFactory()

        response = auth_admin.delete(
            self.endpoint.format(id=contact_phone.id),
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT

        contact_phone.refresh_from_db()

        assert contact_phone.deleted_at is not None
        assert contact_phone.is_deleted is True


class TestContactPhoneRestore:
    endpoint = "/api/v1/contacts/phone/{id}/restore/"

    def test_restores_contact_phone(
        self,
        auth_admin,
    ):
        contact_phone = ContactPhoneFactory()

        contact_phone.soft_delete()

        response = auth_admin.post(
            self.endpoint.format(id=contact_phone.id),
        )

        assert response.status_code == status.HTTP_200_OK

        contact_phone.refresh_from_db()

        assert contact_phone.deleted_at is None
        assert contact_phone.is_deleted is False


class TestContactPhoneHardDelete:
    endpoint = "/api/v1/contacts/phone/{id}/hard_delete/"

    def test_hard_deletes_contact_phone(
        self,
        auth_admin,
    ):
        contact_phone = ContactPhoneFactory()

        response = auth_admin.delete(
            self.endpoint.format(id=contact_phone.id),
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT

        assert not ContactPhone.objects.filter(
            id=contact_phone.id,
        ).exists()
