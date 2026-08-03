# backend/leads/tests/test_lead_filters.py

import pytest
from companies.tests.factories import CompanyFactory
from contacts.tests.factories import ContactFactory
from rest_framework import status
from staff.tests.factories import UserFactory

from leads.models import LeadSource, LeadStatus
from leads.tests.factories import LeadFactory

pytestmark = pytest.mark.django_db


class TestLeadSearch:
    endpoint = "/api/v1/leads/"

    def test_search_title(
        self,
        auth_admin,
    ):
        LeadFactory(
            title="Enterprise CRM Implementation",
        )

        LeadFactory(
            title="Hotel Reservation System",
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "search": "Enterprise",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["title"] == "Enterprise CRM Implementation"


class TestLeadFilterStatus:
    endpoint = "/api/v1/leads/"

    def test_filter_status(
        self,
        auth_admin,
    ):
        LeadFactory(
            status=LeadStatus.NEW,
        )

        LeadFactory(
            status=LeadStatus.QUALIFIED,
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "status": LeadStatus.NEW,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["status"] == LeadStatus.NEW


class TestLeadFilterSource:
    endpoint = "/api/v1/leads/"

    def test_filter_source(
        self,
        auth_admin,
    ):
        LeadFactory(
            source=LeadSource.WEBSITE,
        )

        LeadFactory(
            source=LeadSource.REFERRAL,
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "source": LeadSource.WEBSITE,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["source"] == LeadSource.WEBSITE


class TestLeadFilterCompany:
    endpoint = "/api/v1/leads/"

    def test_filter_company(
        self,
        auth_admin,
    ):
        company = CompanyFactory()

        LeadFactory(
            company=company,
        )

        LeadFactory()

        response = auth_admin.get(
            self.endpoint,
            {
                "company": company.id,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1


class TestLeadFilterContact:
    endpoint = "/api/v1/leads/"

    def test_filter_contact(
        self,
        auth_admin,
    ):
        contact = ContactFactory()

        LeadFactory(
            contact=contact,
        )

        LeadFactory()

        response = auth_admin.get(
            self.endpoint,
            {
                "contact": contact.id,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1


class TestLeadFilterOwner:
    endpoint = "/api/v1/leads/"

    def test_filter_owner(
        self,
        auth_admin,
    ):
        owner = UserFactory()

        LeadFactory(
            owner=owner,
        )

        LeadFactory()

        response = auth_admin.get(
            self.endpoint,
            {
                "owner": owner.id,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1


class TestLeadFilterEstimatedValue:
    endpoint = "/api/v1/leads/"

    def test_filter_estimated_value_min(
        self,
        auth_admin,
    ):
        LeadFactory(
            estimated_value="1000.00",
        )

        LeadFactory(
            estimated_value="10000.00",
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "estimated_value_min": 5000,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

    def test_filter_estimated_value_max(
        self,
        auth_admin,
    ):
        LeadFactory(
            estimated_value="1000.00",
        )

        LeadFactory(
            estimated_value="10000.00",
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "estimated_value_max": 5000,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1


class TestLeadFilterProbability:
    endpoint = "/api/v1/leads/"

    def test_filter_probability_min(
        self,
        auth_admin,
    ):
        LeadFactory(
            probability=20,
        )

        LeadFactory(
            probability=80,
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "probability_min": 50,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

    def test_filter_probability_max(
        self,
        auth_admin,
    ):
        LeadFactory(
            probability=20,
        )

        LeadFactory(
            probability=80,
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "probability_max": 50,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1


class TestLeadFilterDates:
    endpoint = "/api/v1/leads/"

    def test_filter_expected_close_date_before(
        self,
        auth_admin,
    ):
        LeadFactory(
            expected_close_date="2026-01-01",
        )

        LeadFactory(
            expected_close_date="2026-12-01",
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "expected_close_before": "2026-06-01",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

    def test_filter_expected_close_date_after(
        self,
        auth_admin,
    ):
        LeadFactory(
            expected_close_date="2026-01-01",
        )

        LeadFactory(
            expected_close_date="2026-12-01",
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "expected_close_after": "2026-06-01",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1


class TestLeadOrdering:
    endpoint = "/api/v1/leads/"

    def test_order_by_estimated_value(
        self,
        auth_admin,
    ):
        LeadFactory(
            estimated_value="5000.00",
        )

        LeadFactory(
            estimated_value="1000.00",
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "ordering": "estimated_value",
            },
        )

        assert response.status_code == status.HTTP_200_OK

        assert response.data[0]["estimated_value"] == "1000.00"

    def test_order_by_created_desc(
        self,
        auth_admin,
    ):
        older = LeadFactory()
        newer = LeadFactory()

        response = auth_admin.get(
            self.endpoint,
            {
                "ordering": "-created_at",
            },
        )

        assert response.status_code == status.HTTP_200_OK

        ids = [item["id"] for item in response.data]

        assert ids.index(str(newer.id)) < ids.index(str(older.id))
