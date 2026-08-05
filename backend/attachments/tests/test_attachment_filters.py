# backend/attachments/tests/test_attachment_filters.py
import pytest
from companies.tests.factories import CompanyFactory
from django.contrib.contenttypes.models import ContentType
from rest_framework import status
from staff.tests.factories import UserFactory

from attachments.tests.factories import AttachmentFactory

pytestmark = pytest.mark.django_db


class TestAttachmentFilterUploadedBy:
    endpoint = "/api/v1/attachments/"

    def test_filter_uploaded_by(
        self,
        auth_admin,
    ):
        user = UserFactory()

        AttachmentFactory(
            uploaded_by=user,
        )

        AttachmentFactory()

        response = auth_admin.get(
            self.endpoint,
            {
                "uploaded_by": user.id,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1


class TestAttachmentFilterContentType:
    endpoint = "/api/v1/attachments/"

    def test_filter_content_type(
        self,
        auth_admin,
    ):
        company = CompanyFactory()

        content_type = ContentType.objects.get_for_model(
            company,
        )

        AttachmentFactory(
            content_object=company,
        )

        AttachmentFactory()

        response = auth_admin.get(
            self.endpoint,
            {
                "content_type": content_type.id,
                "object_id": company.id,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1


class TestAttachmentFilterObjectId:
    endpoint = "/api/v1/attachments/"

    def test_filter_object_id(
        self,
        auth_admin,
    ):
        company = CompanyFactory()

        AttachmentFactory(
            content_object=company,
        )

        AttachmentFactory()

        response = auth_admin.get(
            self.endpoint,
            {
                "object_id": company.id,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1


class TestAttachmentFilterGenericRelation:
    endpoint = "/api/v1/attachments/"

    def test_filter_by_content_type_and_object_id(
        self,
        auth_admin,
    ):
        company = CompanyFactory()

        content_type = ContentType.objects.get_for_model(
            company,
        )

        AttachmentFactory(
            content_object=company,
        )

        AttachmentFactory()

        response = auth_admin.get(
            self.endpoint,
            {
                "content_type": content_type.id,
                "object_id": company.id,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1


class TestAttachmentCreatedAtFilter:
    endpoint = "/api/v1/attachments/"

    def test_filter_created_at_range(
        self,
        auth_admin,
    ):
        attachment = AttachmentFactory()

        created_date = attachment.created_at.date()

        response = auth_admin.get(
            self.endpoint,
            {
                "created_at_after": created_date,
                "created_at_before": created_date,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1
