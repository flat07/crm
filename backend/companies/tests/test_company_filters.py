# backend/companies/tests/test_company_filters.py
import pytest
from rest_framework import status
from staff.tests.factories import UserFactory

from companies.models import CompanySize, CompanyType, Industry
from companies.tests.factories import CompanyFactory

pytestmark = pytest.mark.django_db


class TestCompanySearch:
    endpoint = "/api/v1/companies/"

    def test_search_company_name(
        self,
        auth_admin,
    ):
        CompanyFactory(
            name="Microsoft Corporation",
        )

        CompanyFactory(
            name="Apple Inc",
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "search": "Microsoft",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["name"] == "Microsoft Corporation"


class TestCompanyFilterName:
    endpoint = "/api/v1/companies/"

    def test_filter_name_contains(
        self,
        auth_admin,
    ):
        CompanyFactory(
            name="Global Hotel Solutions",
        )

        CompanyFactory(
            name="Local Cafe",
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "name": "Hotel",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1


class TestCompanyFilterLegalName:
    endpoint = "/api/v1/companies/"

    def test_filter_legal_name_contains(
        self,
        auth_admin,
    ):
        CompanyFactory(
            legal_name="Alisher Technologies LLC",
        )

        CompanyFactory(
            legal_name="Hotel Group LLC",
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "legal_name": "Technologies",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1


class TestCompanyFilterLocation:
    endpoint = "/api/v1/companies/"

    def test_filter_city_contains(
        self,
        auth_admin,
    ):
        CompanyFactory(
            city="Tashkent",
        )

        CompanyFactory(
            city="Dubai",
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "city": "tash",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1

    def test_filter_country_contains(
        self,
        auth_admin,
    ):
        CompanyFactory(
            country="Uzbekistan",
        )

        CompanyFactory(
            country="United Arab Emirates",
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "country": "Uzbek",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1


class TestCompanyFilterEmail:
    endpoint = "/api/v1/companies/"

    def test_filter_email_contains(
        self,
        auth_admin,
    ):
        CompanyFactory(
            email="sales@example.com",
        )

        CompanyFactory(
            email="support@test.com",
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "email": "sales",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1


class TestCompanyFilterIndustry:
    endpoint = "/api/v1/companies/"

    def test_filter_industry(
        self,
        auth_admin,
    ):
        CompanyFactory(
            industry=Industry.TECHNOLOGY,
        )

        CompanyFactory(
            industry=Industry.HOSPITALITY,
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "industry": Industry.TECHNOLOGY,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1


class TestCompanyFilterType:
    endpoint = "/api/v1/companies/"

    def test_filter_company_type(
        self,
        auth_admin,
    ):
        CompanyFactory(
            company_type=CompanyType.CUSTOMER,
        )

        CompanyFactory(
            company_type=CompanyType.PARTNER,
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "company_type": CompanyType.CUSTOMER,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1


class TestCompanyFilterSize:
    endpoint = "/api/v1/companies/"

    def test_filter_company_size(
        self,
        auth_admin,
    ):
        CompanyFactory(
            size=CompanySize.LARGE,
        )

        CompanyFactory(
            size=CompanySize.SMALL,
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "size": CompanySize.LARGE,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1


class TestCompanyFilterOwner:
    endpoint = "/api/v1/companies/"

    def test_filter_owner(
        self,
        auth_admin,
    ):
        owner = UserFactory()

        CompanyFactory(
            owner=owner,
        )

        CompanyFactory()

        response = auth_admin.get(
            self.endpoint,
            {
                "owner": owner.id,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1


class TestCompanyFilterCreatedBy:
    endpoint = "/api/v1/companies/"

    def test_filter_created_by(
        self,
        auth_admin,
    ):
        user = UserFactory()

        CompanyFactory(
            created_by=user,
        )

        CompanyFactory()

        response = auth_admin.get(
            self.endpoint,
            {
                "created_by": user.id,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1


class TestCompanyFilterDates:
    endpoint = "/api/v1/companies/"

    def test_filter_created_after(
        self,
        auth_admin,
    ):
        company = CompanyFactory()

        response = auth_admin.get(
            self.endpoint,
            {
                "created_after": company.created_at,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) >= 1

    def test_filter_created_before(
        self,
        auth_admin,
    ):
        company = CompanyFactory()

        response = auth_admin.get(
            self.endpoint,
            {
                "created_before": company.created_at,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) >= 1


class TestCompanyFilterActive:
    endpoint = "/api/v1/companies/"

    def test_filter_active(
        self,
        auth_admin,
    ):
        CompanyFactory(
            is_active=True,
        )

        CompanyFactory(
            is_active=False,
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "is_active": True,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1


class TestCompanyOrdering:
    endpoint = "/api/v1/companies/"

    def test_order_by_name(
        self,
        auth_admin,
    ):
        CompanyFactory(
            name="Zulu Company",
        )

        CompanyFactory(
            name="Alpha Company",
        )

        response = auth_admin.get(
            self.endpoint,
            {
                "ordering": "name",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data["results"][0]["name"] == "Alpha Company"
