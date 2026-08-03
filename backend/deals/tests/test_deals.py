# backend/deals/tests/test_deals.py

import pytest
from companies.tests.factories import CompanyFactory
from leads.tests.factories import LeadFactory
from rest_framework import status

from deals.models import Deal, DealStage
from deals.tests.factories import DealFactory

pytestmark = pytest.mark.django_db


class TestDealList:
    endpoint = "/api/v1/deals/"

    def test_returns_deal_list(self, auth_admin):
        DealFactory.create_batch(3)

        response = auth_admin.get(self.endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3


class TestDealRetrieve:
    endpoint = "/api/v1/deals/{id}/"

    def test_returns_deal_detail(self, auth_admin):
        deal = DealFactory()

        response = auth_admin.get(
            self.endpoint.format(id=deal.id),
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == str(deal.id)
        assert response.data["stage"] == deal.stage

    def test_returns_404_for_unknown_deal(
        self,
        auth_admin,
    ):
        response = auth_admin.get(
            "/api/v1/deals/00000000-0000-0000-0000-000000000000/",
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND


class TestDealCreate:
    endpoint = "/api/v1/deals/"

    def test_creates_deal(
        self,
        auth_admin,
    ):
        lead = LeadFactory()
        company = CompanyFactory()
        payload = {
            "lead": str(lead.id),
            "company": str(company.id),
            "stage": DealStage.PROSPECTING,
            "amount": "15000.00",
            "probability": 20,
            "expected_close_date": "2026-12-31",  # Standard YYYY-MM-DD format
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

        assert Deal.objects.filter(
            lead_id=lead.id,
        ).exists()

    def test_requires_name(self, auth_admin):
        response = auth_admin.post(
            self.endpoint,
            {},
            format="json",
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "lead" in response.data


class TestDealUpdate:
    def test_updates_deal(
        self,
        auth_admin,
    ):
        lead = LeadFactory()
        lead2 = LeadFactory()
        deal = DealFactory(
            lead_id=lead.id,
        )

        response = auth_admin.patch(
            f"/api/v1/deals/{deal.id}/",
            {
                "lead": lead2.id,
            },
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK

        deal.refresh_from_db()

        assert deal.lead.id == lead2.id


class TestDealDelete:
    endpoint = "/api/v1/deals/{id}/"

    def test_soft_deletes_deal(
        self,
        auth_admin,
    ):
        deal = DealFactory()

        response = auth_admin.delete(
            self.endpoint.format(id=deal.id),
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT

        deal.refresh_from_db()

        assert deal.deleted_at is not None
        assert deal.is_deleted is True
