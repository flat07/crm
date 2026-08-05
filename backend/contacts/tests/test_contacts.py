# backend/contacts/tests/test_contacts.py

import pytest
from companies.tests.factories import CompanyFactory
from rest_framework import status

from contacts.models import Contact, ContactSource, ContactType
from contacts.tests.factories import ContactFactory

pytestmark = pytest.mark.django_db


class TestCompanyList:
    endpoint = "/api/v1/contacts/"

    def test_returns_contact_list(self, auth_admin):
        ContactFactory.create_batch(3)

        response = auth_admin.get(self.endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3


class TestCompanyRetrieve:
    endpoint = "/api/v1/contacts/{id}/"

    def test_returns_contact_detail(self, auth_admin):
        contact = ContactFactory()

        response = auth_admin.get(
            self.endpoint.format(id=contact.id),
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == str(contact.id)
        assert response.data["first_name"] == contact.first_name

    def test_returns_404_for_unknown_contact(
        self,
        auth_admin,
    ):
        response = auth_admin.get(
            "/api/v1/contacts/00000000-0000-0000-0000-000000000000/",
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND


class TestCompanyCreate:
    endpoint = "/api/v1/contacts/"

    def test_creates_contact(
        self,
        auth_admin,
    ):
        company = CompanyFactory()
        payload = {
            "first_name": "John",
            "last_name": "Doe",
            "contact_type": ContactType.CUSTOMER,
            "source": ContactSource.WEBSITE,
            "company": str(company.id),
            "city": "San Francisco",
            "country": "United States",
        }

        response = auth_admin.post(
            self.endpoint,
            payload,
            format="json",
        )
        # print(response.status_code)
        # print(response.data)

        assert response.status_code == status.HTTP_201_CREATED

        assert Contact.objects.filter(
            first_name="John",
        ).exists()

    def test_requires_name(self, auth_admin):
        response = auth_admin.post(
            self.endpoint,
            {},
            format="json",
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "first_name" in response.data


class TestCompanyUpdate:
    def test_updates_contact(
        self,
        auth_admin,
    ):
        contact = ContactFactory(
            first_name="Old Name",
        )

        response = auth_admin.patch(
            f"/api/v1/contacts/{contact.id}/",
            {
                "first_name": "New Name",
            },
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK

        contact.refresh_from_db()

        assert contact.first_name == "New Name"


class TestCompanyDelete:
    endpoint = "/api/v1/contacts/{id}/"

    def test_soft_deletes_contact(
        self,
        auth_admin,
    ):
        contact = ContactFactory()

        response = auth_admin.delete(
            self.endpoint.format(id=contact.id),
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT

        contact.refresh_from_db()

        assert contact.deleted_at is not None
        assert contact.is_deleted is True
