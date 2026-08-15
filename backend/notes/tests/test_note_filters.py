# backend/notes/tests/test_note_filters.py

import pytest
from companies.tests.factories import CompanyFactory
from django.contrib.contenttypes.models import ContentType
from rest_framework import status
from staff.tests.factories import UserFactory

from notes.tests.factories import NoteFactory

pytestmark = pytest.mark.django_db


class TestNoteSearch:
    endpoint = "/api/v1/notes/"

    def test_search_title(
        self,
        auth_admin,
    ):
        NoteFactory(title="Contract renewal")
        NoteFactory(title="Follow-up call")

        response = auth_admin.get(
            self.endpoint,
            {"search": "renewal"},
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["title"] == ("Contract renewal")

    def test_search_content(
        self,
        auth_admin,
    ):
        NoteFactory(
            title="First note",
            content="Discussed the contract renewal.",
        )
        NoteFactory(
            title="Second note",
            content="Send the proposal tomorrow.",
        )

        response = auth_admin.get(
            self.endpoint,
            {"search": "proposal"},
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["title"] == ("Second note")


class TestNoteFilterPinned:
    endpoint = "/api/v1/notes/"

    def test_filter_pinned(
        self,
        auth_admin,
    ):
        NoteFactory(
            title="Pinned note",
            is_pinned=True,
        )
        NoteFactory(
            title="Normal note",
            is_pinned=False,
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "is_pinned": "true",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["title"] == ("Pinned note")


class TestNoteFilterPrivate:
    endpoint = "/api/v1/notes/"

    def test_filter_private(
        self,
        auth_admin,
    ):
        NoteFactory(
            title="Private note",
            is_private=True,
        )
        NoteFactory(
            title="Public note",
            is_private=False,
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "is_private": "true",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["title"] == ("Private note")


class TestNoteFilterCreatedBy:
    endpoint = "/api/v1/notes/"

    def test_filter_created_by(
        self,
        auth_admin,
    ):
        user = UserFactory()

        NoteFactory(created_by=user)
        NoteFactory()

        response = auth_admin.get(
            self.endpoint,
            {
                "created_by": user.id,
            },
        )
        # print("DEBUG: status =", response.status_code)
        # print("DEBUG: data =", response.data)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["created_by"] == (str(user.id))


class TestNoteFilterRelatedObject:
    endpoint = "/api/v1/notes/"

    def test_filter_related_company(
        self,
        auth_admin,
    ):
        company = CompanyFactory()

        NoteFactory(
            content_type=ContentType.objects.get_for_model(
                company,
            ),
            object_id=company.pk,
        )

        NoteFactory()

        response = auth_admin.get(
            self.endpoint,
            {
                "content_type": "company",
                "object_id": str(company.pk),
            },
        )
        # print("DEBUG: status =", response.status_code)
        # print("DEBUG: data =", response.data)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1


class TestNoteOrdering:
    endpoint = "/api/v1/notes/"

    def test_order_by_title(
        self,
        auth_admin,
    ):
        NoteFactory(title="Zebra note")
        NoteFactory(title="Alpha note")

        response = auth_admin.get(
            self.endpoint,
            {
                "ordering": "title",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data["results"][0]["title"] == ("Alpha note")

    def test_order_by_created_desc(
        self,
        auth_admin,
    ):
        older = NoteFactory()
        newer = NoteFactory()

        response = auth_admin.get(
            self.endpoint,
            {
                "ordering": "-created_at",
            },
        )

        assert response.status_code == status.HTTP_200_OK

        ids = [item["id"] for item in response.data["results"]]

        assert ids.index(str(newer.id)) < ids.index(str(older.id))
