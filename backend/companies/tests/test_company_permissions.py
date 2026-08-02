# backend/companies/tests/test_company_permissions.py

import pytest
from rest_framework import status

from companies.tests.factories import CompanyFactory

pytestmark = pytest.mark.django_db


class TestCompanyPermissions:
    endpoint = "/api/v1/companies/"

    def test_list_requires_view_permission(
        self,
        auth_client_no_permissions,
    ):
        response = auth_client_no_permissions.get(self.endpoint)

        assert response.status_code == status.HTTP_403_FORBIDDEN


class TestCompanyList:
    endpoint = "/api/v1/companies/"

    def test_returns_company_list(
        self,
        auth_client_with_company_permissions,
    ):
        CompanyFactory.create_batch(3)

        response = auth_client_with_company_permissions.get(
            self.endpoint,
        )

        assert response.status_code == status.HTTP_200_OK
