# backend/activities/tests/test_activity_permissions.py
import pytest
from rest_framework import status

from activities.tests.factories import ActivityFactory

pytestmark = pytest.mark.django_db


class TestActivityPermissions:
    endpoint = "/api/v1/activities/"

    def test_list_requires_view_permission(
        self,
        auth_client_no_permissions,
    ):
        response = auth_client_no_permissions.get(
            self.endpoint,
        )

        assert response.status_code == status.HTTP_403_FORBIDDEN


class TestActivityList:
    endpoint = "/api/v1/activities/"

    def test_returns_activity_list(
        self,
        auth_client_with_activity_permissions,
    ):
        ActivityFactory.create_batch(3)

        response = auth_client_with_activity_permissions.get(
            self.endpoint,
        )

        assert response.status_code == status.HTTP_200_OK

        assert len(response.data["results"]) == 3
