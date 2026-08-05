# backend/activities/tests/test_activities.py
import pytest
from companies.tests.factories import CompanyFactory
from django.contrib.contenttypes.models import ContentType
from rest_framework import status

from activities.models import (
    Activity,
    ActivityPriority,
    ActivityStatus,
    ActivityType,
)
from activities.tests.factories import ActivityFactory

pytestmark = pytest.mark.django_db


class TestActivityList:
    endpoint = "/api/v1/activities/"

    def test_returns_activity_list(self, auth_admin):
        ActivityFactory.create_batch(3)

        response = auth_admin.get(self.endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 3


class TestActivityRetrieve:
    endpoint = "/api/v1/activities/{id}/"

    def test_returns_activity_detail(
        self,
        auth_admin,
    ):
        activity = ActivityFactory()

        response = auth_admin.get(
            self.endpoint.format(id=activity.id),
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == str(activity.id)
        assert response.data["title"] == activity.title

    def test_returns_404_for_unknown_activity(
        self,
        auth_admin,
    ):
        response = auth_admin.get(
            "/api/v1/activities/00000000-0000-0000-0000-000000000000/",
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND


class TestActivityCreate:
    endpoint = "/api/v1/activities/"

    def test_creates_activity(
        self,
        auth_admin,
    ):
        company = CompanyFactory()

        payload = {
            "title": "Call customer",
            "description": "Discuss pricing and implementation.",
            "activity_type": ActivityType.CALL,
            "status": ActivityStatus.PLANNED,
            "priority": ActivityPriority.HIGH,
            "due_date": "2026-12-31T10:00:00Z",
            "content_type": ContentType.objects.get_for_model(company).pk,
            "object_id": str(company.pk),
        }

        response = auth_admin.post(
            self.endpoint,
            payload,
            format="json",
        )

        assert response.status_code == status.HTTP_201_CREATED

        assert Activity.objects.filter(
            title="Call customer",
        ).exists()

    def test_requires_title(
        self,
        auth_admin,
    ):
        response = auth_admin.post(
            self.endpoint,
            {},
            format="json",
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "title" in response.data


class TestActivityUpdate:
    def test_updates_activity(
        self,
        auth_admin,
    ):
        activity = ActivityFactory()

        response = auth_admin.patch(
            f"/api/v1/activities/{activity.id}/",
            {
                "title": "Follow-up meeting",
                "status": ActivityStatus.COMPLETED,
            },
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK

        activity.refresh_from_db()

        assert activity.title == "Follow-up meeting"
        assert activity.status == ActivityStatus.COMPLETED


class TestActivityDelete:
    endpoint = "/api/v1/activities/{id}/"

    def test_soft_deletes_activity(
        self,
        auth_admin,
    ):
        activity = ActivityFactory()

        response = auth_admin.delete(
            self.endpoint.format(id=activity.id),
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT

        activity.refresh_from_db()

        assert activity.deleted_at is not None
        assert activity.is_deleted is True
