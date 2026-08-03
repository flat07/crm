# backend/leads/tests/test_lead_permissions.py

import pytest
from rest_framework import status

from leads.tests.factories import LeadFactory

pytestmark = pytest.mark.django_db


class TestCompanyPermissions:
    endpoint = "/api/v1/leads/"

    def test_list_requires_view_permission(
        self,
        auth_client_no_permissions,
    ):
        response = auth_client_no_permissions.get(self.endpoint)

        assert response.status_code == status.HTTP_403_FORBIDDEN


class TestCompanyList:
    endpoint = "/api/v1/leads/"

    def test_returns_lead_list(
        self,
        auth_client_with_lead_permissions,
    ):
        LeadFactory.create_batch(3)

        response = auth_client_with_lead_permissions.get(
            self.endpoint,
        )

        assert response.status_code == status.HTTP_200_OK
