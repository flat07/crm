# backend/activities/tests/test_attachments.py
import pytest
from companies.tests.factories import CompanyFactory
from django.contrib.contenttypes.models import ContentType
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status

from attachments.models import Attachment
from attachments.tests.factories import AttachmentFactory

pytestmark = pytest.mark.django_db


class TestAttachmentList:
    endpoint = "/api/v1/attachments/"

    def test_returns_attachment_list(
        self,
        auth_admin,
    ):
        AttachmentFactory.create_batch(3)

        response = auth_admin.get(
            self.endpoint,
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3


class TestAttachmentRetrieve:
    endpoint = "/api/v1/attachments/{id}/"

    def test_returns_attachment_detail(
        self,
        auth_admin,
    ):
        attachment = AttachmentFactory()

        response = auth_admin.get(
            self.endpoint.format(
                id=attachment.id,
            ),
        )

        assert response.status_code == status.HTTP_200_OK

        assert response.data["id"] == str(attachment.id)

        assert response.data["filename"] == attachment.filename

    def test_returns_404_for_unknown_attachment(
        self,
        auth_admin,
    ):
        response = auth_admin.get(
            "/api/v1/attachments/00000000-0000-0000-0000-000000000000/",
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND


class TestAttachmentCreate:
    endpoint = "/api/v1/attachments/"

    def test_creates_attachment(
        self,
        auth_admin,
    ):
        company = CompanyFactory()

        content_type = ContentType.objects.get_for_model(
            company,
        )

        payload = {
            "file": SimpleUploadedFile(
                name="contract.txt",
                content=b"Contract document",
                content_type="text/plain",
            ),
            "filename": "contract.txt",
            "description": "Customer contract",
            "mime_type": "text/plain",
            "content_type": content_type.id,
            "object_id": str(company.id),
        }

        response = auth_admin.post(
            self.endpoint,
            payload,
            format="multipart",
        )
        print(response.status_code)
        print(response.data)

        assert response.status_code == status.HTTP_201_CREATED

        assert Attachment.objects.filter(
            filename="contract.txt",
        ).exists()

    def test_requires_file(
        self,
        auth_admin,
    ):
        response = auth_admin.post(
            self.endpoint,
            {},
            format="multipart",
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST

        assert "file" in response.data


class TestAttachmentUpdate:
    def test_updates_attachment(
        self,
        auth_admin,
    ):
        attachment = AttachmentFactory()

        response = auth_admin.patch(
            f"/api/v1/attachments/{attachment.id}/",
            {
                "description": "Updated description",
            },
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK

        attachment.refresh_from_db()

        assert attachment.description == "Updated description"


class TestAttachmentDelete:
    endpoint = "/api/v1/attachments/{id}/"

    def test_soft_deletes_attachment(
        self,
        auth_admin,
    ):
        attachment = AttachmentFactory()

        response = auth_admin.delete(
            self.endpoint.format(
                id=attachment.id,
            ),
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT

        attachment.refresh_from_db()

        assert attachment.deleted_at is not None
        assert attachment.is_deleted is True


class TestAttachmentGenericRelation:
    def test_attachment_belongs_to_company(
        self,
        auth_admin,
    ):
        company = CompanyFactory()

        AttachmentFactory(
            content_object=company,
        )

        response = auth_admin.get(
            "/api/v1/attachments/",
            {
                "content_type": ContentType.objects.get_for_model(company).id,
                "object_id": company.id,
            },
        )

        assert response.status_code == 200
        assert len(response.data) == 1
