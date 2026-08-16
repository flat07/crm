# backend/notes/tests/test_notes.py

import pytest
from companies.tests.factories import CompanyFactory
from django.contrib.contenttypes.models import ContentType
from rest_framework import status

from notes.models import Note
from notes.tests.factories import NoteFactory

pytestmark = pytest.mark.django_db


class TestNoteList:
    endpoint = "/api/v1/notes/"

    def test_returns_note_list(
        self,
        auth_admin,
    ):
        NoteFactory.create_batch(3)

        response = auth_admin.get(self.endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 3


class TestNoteRetrieve:
    endpoint = "/api/v1/notes/{id}/"

    def test_returns_note_detail(
        self,
        auth_admin,
    ):
        note = NoteFactory()

        response = auth_admin.get(
            self.endpoint.format(id=note.id),
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == str(note.id)
        assert response.data["title"] == note.title
        assert response.data["content"] == note.content

    def test_returns_404_for_unknown_note(
        self,
        auth_admin,
    ):
        response = auth_admin.get(
            "/api/v1/notes/00000000-0000-0000-0000-000000000000/",
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND


class TestNoteCreate:
    endpoint = "/api/v1/notes/"

    def test_creates_note(
        self,
        auth_admin,
    ):
        company = CompanyFactory()

        payload = {
            "title": "Call with John",
            "content": "Discussed renewal for contract.",
            "content_type": "company",
            "object_id": str(company.pk),
            "is_pinned": False,
            "is_private": False,
        }

        response = auth_admin.post(
            self.endpoint,
            payload,
            format="json",
        )
        # print("DEBUG: status =", response.status_code)
        # print("DEBUG: data =", response.data)

        assert response.status_code == status.HTTP_201_CREATED

        assert Note.objects.filter(
            title="Call with John",
        ).exists()

        note = Note.objects.get(
            title="Call with John",
        )

        assert note.content == ("Discussed renewal for contract.")
        assert note.object_id == company.pk
        assert response.data["title"] == "Call with John"
        assert response.data["content"] == "Discussed renewal for contract."
        assert response.data["content_type"] == "company"
        assert response.data["object_id"] == str(company.pk)

    def test_requires_content(
        self,
        auth_admin,
    ):
        response = auth_admin.post(
            self.endpoint,
            {
                "title": "Empty note",
            },
            format="json",
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "content" in response.data

    def test_requires_content_object(
        self,
        auth_admin,
    ):
        response = auth_admin.post(
            self.endpoint,
            {
                "title": "Note without target",
                "content": "Some content",
            },
            format="json",
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST


class TestNoteUpdate:
    endpoint = "/api/v1/notes/"

    def test_updates_note(
        self,
        auth_admin,
    ):
        note = NoteFactory()

        response = auth_admin.patch(
            f"{self.endpoint}{note.id}/",
            {
                "title": "Follow-up",
                "content": "Send proposal tomorrow.",
            },
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK

        note.refresh_from_db()

        assert note.title == "Follow-up"
        assert note.content == "Send proposal tomorrow."

    def test_updates_note_content(
        self,
        auth_admin,
    ):
        note = NoteFactory(
            title="Old title",
            content="Old content",
        )

        response = auth_admin.patch(
            f"{self.endpoint}{note.id}/",
            {
                "title": "Updated title",
                "content": "Updated content",
            },
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK

        note.refresh_from_db()

        assert note.title == "Updated title"
        assert note.content == "Updated content"

    def test_updates_related_object(
        self,
        auth_admin,
    ):
        company1 = CompanyFactory()
        company2 = CompanyFactory()

        note = NoteFactory(
            content_type=ContentType.objects.get_for_model(company1),
            object_id=company1.id,
        )

        response = auth_admin.patch(
            f"{self.endpoint}{note.id}/",
            {
                "content_type": "company",
                "object_id": str(company2.id),
            },
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK

        note.refresh_from_db()

        assert note.content_type == ContentType.objects.get_for_model(
            company2,
        )
        assert note.object_id == company2.id


class TestNoteDelete:
    endpoint = "/api/v1/notes/{id}/"

    def test_soft_deletes_note(
        self,
        auth_admin,
    ):
        note = NoteFactory()

        response = auth_admin.delete(
            self.endpoint.format(id=note.id),
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT

        note.refresh_from_db()

        assert note.deleted_at is not None
        assert note.is_deleted is True


class TestNoteRestore:
    endpoint = "/api/v1/notes/{id}/restore/"

    def test_restores_note(
        self,
        auth_admin,
    ):
        note = NoteFactory()

        note.soft_delete()

        note.refresh_from_db()

        assert note.is_deleted is True

        response = auth_admin.post(
            self.endpoint.format(id=note.id),
        )

        assert response.status_code == status.HTTP_200_OK

        note.refresh_from_db()

        assert note.is_deleted is False
        assert note.deleted_at is None


class TestNoteHardDelete:
    endpoint = "/api/v1/notes/{id}/hard_delete/"

    def test_hard_deletes_note(
        self,
        auth_admin,
    ):
        note = NoteFactory()

        note_id = note.id

        response = auth_admin.delete(
            self.endpoint.format(id=note_id),
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT

        assert not Note.objects.filter(
            id=note_id,
        ).exists()


class TestNotePin:
    endpoint = "/api/v1/notes/{id}/toggle_pin/"

    def test_pins_note(
        self,
        auth_admin,
    ):
        note = NoteFactory(is_pinned=False)

        response = auth_admin.post(
            self.endpoint.format(id=note.id),
        )

        assert response.status_code == status.HTTP_200_OK

        note.refresh_from_db()

        assert note.is_pinned is True

    def test_unpins_note(
        self,
        auth_admin,
    ):
        note = NoteFactory(is_pinned=True)

        response = auth_admin.post(
            self.endpoint.format(id=note.id),
        )

        assert response.status_code == status.HTTP_200_OK

        note.refresh_from_db()

        assert note.is_pinned is False


class TestNotePrivate:
    endpoint = "/api/v1/notes/{id}/toggle_private/"

    def test_makes_note_private(
        self,
        auth_admin,
    ):
        note = NoteFactory(is_private=False)

        response = auth_admin.post(
            self.endpoint.format(id=note.id),
        )

        assert response.status_code == status.HTTP_200_OK

        note.refresh_from_db()

        assert note.is_private is True

    def test_makes_note_public(
        self,
        auth_admin,
    ):
        note = NoteFactory(is_private=True)

        response = auth_admin.post(
            self.endpoint.format(id=note.id),
        )

        assert response.status_code == status.HTTP_200_OK

        note.refresh_from_db()

        assert note.is_private is False
