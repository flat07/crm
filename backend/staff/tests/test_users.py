# backend/staff/tests/test_users.py
import pytest
from rest_framework import status

from staff.models import User
from staff.tests.factories import UserFactory

pytestmark = pytest.mark.django_db


class TestUserList:
    endpoint = "/api/v1/auth/users/"

    def test_returns_users(
        self,
        auth_admin,
    ):
        initial_count = User.objects.count()
        UserFactory.create_batch(3)

        response = auth_admin.get(self.endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == initial_count + 3


class TestUserRetrieve:
    def test_returns_user(
        self,
        auth_admin,
    ):
        user = UserFactory()

        response = auth_admin.get(f"/api/v1/auth/users/{user.id}/")

        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == str(user.id)


class TestUserCreate:
    endpoint = "/api/v1/auth/users/"

    def test_creates_user(
        self,
        auth_admin,
    ):
        payload = {
            "email": "john@example.com",
            "first_name": "John",
            "last_name": "Doe",
            "password": "password123",
        }

        response = auth_admin.post(
            self.endpoint,
            payload,
            format="json",
        )

        assert response.status_code == status.HTTP_201_CREATED

        assert User.objects.filter(email="john@example.com").exists()


class TestUserUpdate:
    def test_updates_user(
        self,
        auth_admin,
    ):
        user = UserFactory()

        response = auth_admin.patch(
            f"/api/v1/auth/users/{user.id}/",
            {
                "first_name": "Updated",
            },
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK

        user.refresh_from_db()

        assert user.first_name == "Updated"


class TestUserDelete:
    def test_deletes_user(
        self,
        auth_admin,
    ):
        user = UserFactory()

        response = auth_admin.delete(f"/api/v1/auth/users/{user.id}/")

        assert response.status_code == status.HTTP_204_NO_CONTENT

        assert not User.objects.filter(pk=user.pk).exists()


class TestPermissions:
    endpoint = "/api/v1/auth/users/"

    def test_anonymous_cannot_access(
        self,
        api_client,
    ):
        response = api_client.get(self.endpoint)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_non_admin_cannot_access(
        self,
        api_client,
        sales_manager,
    ):
        api_client.force_authenticate(sales_manager)

        response = api_client.get(self.endpoint)

        assert response.status_code == status.HTTP_403_FORBIDDEN
