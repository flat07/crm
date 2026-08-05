# backend/companies/tests/test_companies.py

import pytest
from rest_framework import status

from companies.models import Company, CompanyType, Industry
from companies.tests.factories import CompanyFactory

pytestmark = pytest.mark.django_db


class TestCompanyList:
    endpoint = "/api/v1/companies/"

    def test_returns_company_list(self, auth_admin):
        CompanyFactory.create_batch(3)

        response = auth_admin.get(self.endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == Company.objects.count()
        assert len(response.data["results"]) == 3


class TestCompanyRetrieve:
    endpoint = "/api/v1/companies/{id}/"

    def test_returns_company_detail(self, auth_admin):
        company = CompanyFactory()

        response = auth_admin.get(
            self.endpoint.format(id=company.id),
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == str(company.id)
        assert response.data["name"] == company.name

    def test_returns_404_for_unknown_company(
        self,
        auth_admin,
    ):
        response = auth_admin.get(
            "/api/v1/companies/00000000-0000-0000-0000-000000000000/",
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND


class TestCompanyCreate:
    endpoint = "/api/v1/companies/"

    def test_creates_company(
        self,
        auth_admin,
    ):
        payload = {
            "name": "OpenAI",
            "industry": Industry.TECHNOLOGY,
            "company_type": CompanyType.CUSTOMER,
            "city": "San Francisco",
            "country": "United States",
        }

        response = auth_admin.post(
            self.endpoint,
            payload,
            format="json",
        )

        assert response.status_code == status.HTTP_201_CREATED

        assert Company.objects.filter(
            name="OpenAI",
        ).exists()

    def test_requires_name(self, auth_admin):
        response = auth_admin.post(
            self.endpoint,
            {},
            format="json",
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "name" in response.data


class TestCompanyUpdate:
    def test_updates_company(
        self,
        auth_admin,
    ):
        company = CompanyFactory(
            name="Old Name",
        )

        response = auth_admin.patch(
            f"/api/v1/companies/{company.id}/",
            {
                "name": "New Name",
            },
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK

        company.refresh_from_db()

        assert company.name == "New Name"


class TestCompanyDelete:
    endpoint = "/api/v1/companies/{id}/"

    def test_soft_deletes_company(
        self,
        auth_admin,
    ):
        company = CompanyFactory()

        response = auth_admin.delete(
            self.endpoint.format(id=company.id),
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT

        company.refresh_from_db()

        assert company.deleted_at is not None
        assert company.is_deleted is True
