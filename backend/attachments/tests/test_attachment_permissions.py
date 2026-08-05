# backend/activities/tests/test_attachment_permissions.py
import pytest
from rest_framework import status

from attachments.tests.factories import AttachmentFactory

pytestmark = pytest.mark.django_db


class TestAttachmentPermissions:
    endpoint = "/api/v1/attachments/"

    def test_list_requires_view_permission(
        self,
        auth_client_no_permissions,
    ):
        response = auth_client_no_permissions.get(
            self.endpoint,
        )

        assert response.status_code == status.HTTP_403_FORBIDDEN


class TestAttachmentList:
    endpoint = "/api/v1/attachments/"

    def test_returns_attachment_list(
        self,
        auth_client_with_attachment_permissions,
    ):
        AttachmentFactory.create_batch(3)

        response = auth_client_with_attachment_permissions.get(
            self.endpoint,
        )

        assert response.status_code == status.HTTP_200_OK

        assert len(response.data) == 3
