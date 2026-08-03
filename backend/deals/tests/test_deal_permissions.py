# backend/deals/tests/test_deal_permissions.py

import pytest
from rest_framework import status

from deals.tests.factories import DealFactory

pytestmark = pytest.mark.django_db


class TestCompanyPermissions:
    endpoint = "/api/v1/deals/"

    def test_list_requires_view_permission(
        self,
        auth_client_no_permissions,
    ):
        response = auth_client_no_permissions.get(self.endpoint)

        assert response.status_code == status.HTTP_403_FORBIDDEN


class TestCompanyList:
    endpoint = "/api/v1/deals/"

    def test_returns_deal_list(
        self,
        auth_client_with_deal_permissions,
    ):
        DealFactory.create_batch(3)

        response = auth_client_with_deal_permissions.get(
            self.endpoint,
        )

        assert response.status_code == status.HTTP_200_OK
