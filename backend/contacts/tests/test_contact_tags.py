# backend/contacts/tests/test_contact_tags.py

import pytest
from rest_framework import status

from contacts.models import ContactTag
from contacts.tests.factories import ContactTagFactory

pytestmark = pytest.mark.django_db


class TestContactTagList:
    endpoint = "/api/v1/contacts/tags/"

    def test_returns_contact_tag_list(self, auth_admin):
        ContactTagFactory.create_batch(3)

        response = auth_admin.get(self.endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 3


class TestContactTagRetrieve:
    endpoint = "/api/v1/contacts/tags/{id}/"

    def test_returns_contact_tag_detail(
        self,
        auth_admin,
    ):
        tag = ContactTagFactory()

        response = auth_admin.get(
            self.endpoint.format(id=tag.id),
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == str(tag.id)
        assert response.data["name"] == tag.name

    def test_returns_404_for_unknown_tag(
        self,
        auth_admin,
    ):
        response = auth_admin.get(
            self.endpoint.format(
                id="00000000-0000-0000-0000-000000000000",
            ),
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND


class TestContactTagCreate:
    endpoint = "/api/v1/contacts/tags/"

    def test_creates_contact_tag(
        self,
        auth_admin,
    ):
        payload = {
            "name": "VIP",
        }

        response = auth_admin.post(
            self.endpoint,
            payload,
            format="json",
        )

        assert response.status_code == status.HTTP_201_CREATED

        assert ContactTag.objects.filter(
            name="VIP",
        ).exists()

    def test_requires_name(
        self,
        auth_admin,
    ):
        response = auth_admin.post(
            self.endpoint,
            {},
            format="json",
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "name" in response.data


class TestContactTagUpdate:
    def test_updates_contact_tag(
        self,
        auth_admin,
    ):
        tag = ContactTagFactory(
            name="Regular",
        )

        response = auth_admin.patch(
            f"/api/v1/contacts/tags/{tag.id}/",
            {
                "name": "VIP",
            },
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK

        tag.refresh_from_db()

        assert tag.name == "VIP"


class TestContactTagDelete:
    endpoint = "/api/v1/contacts/tags/{id}/"

    def test_soft_deletes_contact_tag(
        self,
        auth_admin,
    ):
        tag = ContactTagFactory()

        response = auth_admin.delete(
            self.endpoint.format(id=tag.id),
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT

        tag.refresh_from_db()

        assert tag.deleted_at is not None
        assert tag.is_deleted is True


class TestContactTagRestore:
    endpoint = "/api/v1/contacts/tags/{id}/restore/"

    def test_restores_contact_tag(
        self,
        auth_admin,
    ):
        tag = ContactTagFactory()

        tag.soft_delete()

        response = auth_admin.post(
            self.endpoint.format(id=tag.id),
        )

        assert response.status_code == status.HTTP_200_OK

        tag.refresh_from_db()

        assert tag.is_deleted is False
        assert tag.deleted_at is None


class TestContactTagHardDelete:
    endpoint = "/api/v1/contacts/tags/{id}/hard_delete/"

    def test_hard_deletes_contact_tag(
        self,
        auth_admin,
    ):
        tag = ContactTagFactory()

        response = auth_admin.delete(
            self.endpoint.format(id=tag.id),
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT

        assert not ContactTag.objects.filter(
            id=tag.id,
        ).exists()
