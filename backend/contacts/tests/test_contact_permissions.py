# backend/contacts/tests/test_contact_permissions.py

import pytest
from rest_framework import status

from contacts.tests.factories import ContactFactory

pytestmark = pytest.mark.django_db


class TestCompanyPermissions:
    endpoint = "/api/v1/contacts/"

    def test_list_requires_view_permission(
        self,
        auth_client_no_permissions,
    ):
        response = auth_client_no_permissions.get(self.endpoint)

        assert response.status_code == status.HTTP_403_FORBIDDEN


class TestCompanyList:
    endpoint = "/api/v1/contacts/"

    def test_returns_contact_list(
        self,
        auth_client_with_contact_permissions,
    ):
        ContactFactory.create_batch(3)

        response = auth_client_with_contact_permissions.get(
            self.endpoint,
        )

        assert response.status_code == status.HTTP_200_OK
