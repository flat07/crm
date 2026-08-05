# backend/deals/tests/test_deal_filters.py
import pytest
from companies.tests.factories import CompanyFactory
from contacts.tests.factories import ContactFactory
from leads.tests.factories import LeadFactory
from rest_framework import status
from staff.tests.factories import UserFactory

from deals.models import DealStage
from deals.tests.factories import DealFactory

pytestmark = pytest.mark.django_db


class TestDealSearch:
    endpoint = "/api/v1/deals/"

    def test_search_company_name(
        self,
        auth_admin,
    ):
        DealFactory(
            company__name="Enterprise Software",
        )

        DealFactory(
            company__name="Small Business",
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "search": "Enterprise",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1


class TestDealFilterStage:
    endpoint = "/api/v1/deals/"

    def test_filter_stage(
        self,
        auth_admin,
    ):
        DealFactory(
            stage=DealStage.PROPOSAL,
        )

        DealFactory(
            stage=DealStage.WON,
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "stage": DealStage.PROPOSAL,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["stage"] == DealStage.PROPOSAL


class TestDealFilterCompany:
    endpoint = "/api/v1/deals/"

    def test_filter_company(
        self,
        auth_admin,
    ):
        company = CompanyFactory()

        DealFactory(company=company)
        DealFactory()

        response = auth_admin.get(
            self.endpoint,
            {
                "company": company.id,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1


class TestDealFilterLead:
    endpoint = "/api/v1/deals/"

    def test_filter_lead(
        self,
        auth_admin,
    ):
        lead = LeadFactory()

        DealFactory(lead=lead)
        DealFactory()

        response = auth_admin.get(
            self.endpoint,
            {
                "lead": lead.id,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1


class TestDealFilterContact:
    endpoint = "/api/v1/deals/"

    def test_filter_contact(
        self,
        auth_admin,
    ):
        contact = ContactFactory()

        DealFactory(contact=contact)
        DealFactory()

        response = auth_admin.get(
            self.endpoint,
            {
                "contact": contact.id,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1


class TestDealFilterOwner:
    endpoint = "/api/v1/deals/"

    def test_filter_owner(
        self,
        auth_admin,
    ):
        owner = UserFactory()

        DealFactory(owner=owner)
        DealFactory()

        response = auth_admin.get(
            self.endpoint,
            {
                "owner": owner.id,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1


class TestDealFilterAmount:
    endpoint = "/api/v1/deals/"

    def test_filter_amount_min(
        self,
        auth_admin,
    ):
        DealFactory(amount="1000.00")
        DealFactory(amount="5000.00")

        response = auth_admin.get(
            self.endpoint,
            {
                "amount_min": 3000,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1

    def test_filter_amount_max(
        self,
        auth_admin,
    ):
        DealFactory(amount="1000.00")
        DealFactory(amount="5000.00")

        response = auth_admin.get(
            self.endpoint,
            {
                "amount_max": 3000,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1


class TestDealFilterProbability:
    endpoint = "/api/v1/deals/"

    def test_filter_probability_range(
        self,
        auth_admin,
    ):
        DealFactory(probability=20)
        DealFactory(probability=80)

        response = auth_admin.get(
            self.endpoint,
            {
                "probability_min": 50,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1


class TestDealFilterDates:
    endpoint = "/api/v1/deals/"

    def test_filter_expected_close_date(
        self,
        auth_admin,
    ):
        DealFactory(
            expected_close_date="2026-01-01",
        )

        DealFactory(
            expected_close_date="2026-12-01",
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "expected_close_before": "2026-06-01",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1


class TestDealOrdering:
    endpoint = "/api/v1/deals/"

    def test_order_by_amount(
        self,
        auth_admin,
    ):
        DealFactory(
            amount="5000.00",
        )

        DealFactory(
            amount="1000.00",
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "ordering": "amount",
            },
        )

        assert response.status_code == status.HTTP_200_OK

        assert response.data["results"][0]["amount"] == "1000.00"

    def test_order_by_created_desc(
        self,
        auth_admin,
    ):
        older = DealFactory()
        newer = DealFactory()

        response = auth_admin.get(
            self.endpoint,
            {
                "ordering": "-created_at",
            },
        )

        assert response.status_code == status.HTTP_200_OK

        ids = [item["id"] for item in response.data["results"]]

        assert ids.index(str(newer.id)) < ids.index(str(older.id))
