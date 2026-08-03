# backend/activities/tests/test_activity_filters.py
import pytest
from companies.tests.factories import CompanyFactory
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from rest_framework import status
from staff.tests.factories import UserFactory

from activities.models import (
    ActivityPriority,
    ActivityStatus,
    ActivityType,
)
from activities.tests.factories import ActivityFactory

pytestmark = pytest.mark.django_db


class TestActivitySearch:
    endpoint = "/api/v1/activities/"

    def test_search_title(
        self,
        auth_admin,
    ):
        ActivityFactory(title="Team meeting")
        ActivityFactory(title="Phone call")

        response = auth_admin.get(
            self.endpoint,
            {"search": "meeting"},
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["title"] == "Team meeting"


class TestActivityFilterActivityType:
    endpoint = "/api/v1/activities/"

    def test_filter_activity_type(
        self,
        auth_admin,
    ):
        ActivityFactory(activity_type=ActivityType.CALL)
        ActivityFactory(activity_type=ActivityType.EMAIL)

        response = auth_admin.get(
            self.endpoint,
            {
                "activity_type": ActivityType.CALL,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["activity_type"] == ActivityType.CALL


class TestActivityFilterStatus:
    endpoint = "/api/v1/activities/"

    def test_filter_status(
        self,
        auth_admin,
    ):
        ActivityFactory(status=ActivityStatus.COMPLETED)
        ActivityFactory(status=ActivityStatus.PLANNED)

        response = auth_admin.get(
            self.endpoint,
            {
                "status": ActivityStatus.COMPLETED,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["status"] == ActivityStatus.COMPLETED


class TestActivityFilterPriority:
    endpoint = "/api/v1/activities/"

    def test_filter_priority(
        self,
        auth_admin,
    ):
        ActivityFactory(priority=ActivityPriority.HIGH)
        ActivityFactory(priority=ActivityPriority.LOW)

        response = auth_admin.get(
            self.endpoint,
            {
                "priority": ActivityPriority.HIGH,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["priority"] == ActivityPriority.HIGH


class TestActivityFilterOwner:
    endpoint = "/api/v1/activities/"

    def test_filter_owner(
        self,
        auth_admin,
    ):
        owner = UserFactory()

        ActivityFactory(owner=owner)
        ActivityFactory()

        response = auth_admin.get(
            self.endpoint,
            {
                "owner": owner.id,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1


class TestActivityFilterRelatedObject:
    endpoint = "/api/v1/activities/"

    def test_filter_related_company(
        self,
        auth_admin,
    ):
        company = CompanyFactory()

        ActivityFactory(content_object=company)
        ActivityFactory()

        response = auth_admin.get(
            self.endpoint,
            {
                "content_type": ContentType.objects.get_for_model(company).pk,
                "object_id": company.pk,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1


class TestActivityOrdering:
    endpoint = "/api/v1/activities/"

    def test_order_by_due_date(
        self,
        auth_admin,
    ):
        ActivityFactory(
            title="Later",
            due_date=timezone.now() + timezone.timedelta(days=2),
        )

        ActivityFactory(
            title="Soon",
            due_date=timezone.now() + timezone.timedelta(days=1),
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "ordering": "due_date",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data[0]["title"] == "Soon"

    def test_order_by_created_desc(
        self,
        auth_admin,
    ):
        older = ActivityFactory()
        newer = ActivityFactory()

        response = auth_admin.get(
            self.endpoint,
            {
                "ordering": "-created_at",
            },
        )

        assert response.status_code == status.HTTP_200_OK

        ids = [item["id"] for item in response.data]

        assert ids.index(str(newer.id)) < ids.index(str(older.id))
