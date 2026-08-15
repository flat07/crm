# backend/notes/tests/test_note_permissions.py
import pytest
from rest_framework import status

from notes.tests.factories import NoteFactory

pytestmark = pytest.mark.django_db


class TestNotePermissions:
    endpoint = "/api/v1/notes/"

    def test_list_requires_view_permission(
        self,
        auth_client_no_permissions,
    ):
        response = auth_client_no_permissions.get(
            self.endpoint,
        )
        # print("DEBUG: status =", response.status_code)
        # print("DEBUG: data =", response.data)

        assert response.status_code == status.HTTP_403_FORBIDDEN


class TestNoteList:
    endpoint = "/api/v1/notes/"

    def test_returns_note_list(
        self,
        auth_client_with_note_permissions,
    ):
        NoteFactory.create_batch(3)

        response = auth_client_with_note_permissions.get(
            self.endpoint,
        )
        # print("DEBUG: status =", response.status_code)
        # print("DEBUG: data =", response.data)

        assert response.status_code == status.HTTP_200_OK

        assert len(response.data["results"]) == 3
