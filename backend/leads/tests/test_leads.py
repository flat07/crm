# backend/leads/tests/test_leads.py

import pytest
from companies.tests.factories import CompanyFactory
from rest_framework import status

from leads.models import Lead, LeadSource, LeadStatus
from leads.tests.factories import LeadFactory

pytestmark = pytest.mark.django_db


class TestLeadList:
    endpoint = "/api/v1/leads/"

    def test_returns_lead_list(self, auth_admin):
        LeadFactory.create_batch(3)

        response = auth_admin.get(self.endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 3


class TestLeadRetrieve:
    endpoint = "/api/v1/leads/{id}/"

    def test_returns_lead_detail(self, auth_admin):
        lead = LeadFactory()

        response = auth_admin.get(
            self.endpoint.format(id=lead.id),
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == str(lead.id)
        assert response.data["title"] == lead.title

    def test_returns_404_for_unknown_lead(
        self,
        auth_admin,
    ):
        response = auth_admin.get(
            "/api/v1/leads/00000000-0000-0000-0000-000000000000/",
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND


class TestLeadCreate:
    endpoint = "/api/v1/leads/"

    def test_creates_lead(
        self,
        auth_admin,
    ):
        company = CompanyFactory()
        payload = {
            "title": "Enterprise Software Solutions",
            "company_id": str(company.id),
            "source": LeadSource.WEBSITE,
            "status": LeadStatus.NEW,
            "estimated_value": "15000.00",  # Maps to estimated_value field
            "probability": 20,
            "expected_close_date": "2026-12-31",
            "description": "Initial discussion about enterprise package onboarding.",
        }

        response = auth_admin.post(
            self.endpoint,
            payload,
            format="json",
        )
        # print(response.status_code)
        # print(response.data)

        assert response.status_code == status.HTTP_201_CREATED

        assert Lead.objects.filter(
            title="Enterprise Software Solutions",
        ).exists()

    def test_requires_name(self, auth_admin):
        response = auth_admin.post(
            self.endpoint,
            {},
            format="json",
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "title" in response.data


class TestLeadUpdate:
    def test_updates_lead(
        self,
        auth_admin,
    ):
        lead = LeadFactory()

        response = auth_admin.patch(
            f"/api/v1/leads/{lead.id}/",
            {
                "title": "new Enterprise Software Solutions",
            },
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK

        lead.refresh_from_db()

        assert lead.title == "new Enterprise Software Solutions"


class TestLeadDelete:
    endpoint = "/api/v1/leads/{id}/"

    def test_soft_deletes_lead(
        self,
        auth_admin,
    ):
        lead = LeadFactory()

        response = auth_admin.delete(
            self.endpoint.format(id=lead.id),
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT

        lead.refresh_from_db()

        assert lead.deleted_at is not None
        assert lead.is_deleted is True
