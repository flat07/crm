# backend / staff / tests / test_auth.py
import pytest
from rest_framework import status

pytestmark = pytest.mark.django_db


class TestLogin:
    endpoint = "/api/v1/staff/auth/login/"

    def test_login_success(self, api_client, sales_manager):
        response = api_client.post(
            self.endpoint,
            {
                "email": sales_manager.email,
                "password": "password",
            },
            format="json",
        )
        print("DEBUG: response ", response)

        assert response.status_code == status.HTTP_200_OK

        assert "access" in response.data
        assert "refresh" in response.data
        assert "user" in response.data

        payload = response.data["user"]

        assert payload["id"] == str(sales_manager.id)
        assert payload["email"] == sales_manager.email
        assert payload["first_name"] == sales_manager.first_name
        assert payload["last_name"] == sales_manager.last_name

        assert payload["department"] == {
            "id": str(sales_manager.department.id),
            "name": sales_manager.department.name,
        }

        assert payload["roles"] == list(
            sales_manager.roles.values_list(
                "name",
                flat=True,
            )
        )

        assert payload["avatar"] is None
        assert payload["job_title"] == sales_manager.job_title

    def test_invalid_password(self, api_client, sales_manager):
        response = api_client.post(
            self.endpoint,
            {
                "email": sales_manager.email,
                "password": "wrong-password",
            },
            format="json",
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_unknown_email(
        self,
        api_client,
    ):
        response = api_client.post(
            self.endpoint,
            {
                "email": "unknown@example.com",
                "password": "password123",
            },
            format="json",
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


class TestRefreshToken:
    login = "/api/v1/staff/auth/login/"
    refresh = "/api/v1/staff/auth/refresh/"

    def test_refresh_token(
        self,
        api_client,
        sales_manager,
    ):
        login = api_client.post(
            self.login,
            {
                "email": sales_manager.email,
                "password": "password",
            },
            format="json",
        )

        refresh = login.data["refresh"]

        response = api_client.post(
            self.refresh,
            {
                "refresh": refresh,
            },
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK
        assert "access" in response.data

    def test_invalid_refresh_token(
        self,
        api_client,
    ):
        response = api_client.post(
            self.refresh,
            {
                "refresh": "invalid-token",
            },
            format="json",
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


class TestMe:
    endpoint = "/api/v1/staff/auth/me/"

    def test_authenticated_user(
        self,
        api_client,
        sales_manager,
    ):
        api_client.force_authenticate(sales_manager)

        response = api_client.get(self.endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["email"] == sales_manager.email

    def test_anonymous_user(
        self,
        api_client,
    ):
        response = api_client.get(self.endpoint)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


class TestChangePassword:
    endpoint = "/api/v1/staff/auth/change-password/"

    def test_change_password(
        self,
        api_client,
        sales_manager,
    ):
        api_client.force_authenticate(sales_manager)

        response = api_client.post(
            self.endpoint,
            {
                "old_password": "password",
                "new_password": "new-password123",
            },
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK

        sales_manager.refresh_from_db()

        assert sales_manager.check_password("new-password123")

    def test_wrong_old_password(
        self,
        api_client,
        sales_manager,
    ):
        api_client.force_authenticate(sales_manager)

        response = api_client.post(
            self.endpoint,
            {
                "old_password": "wrong-password",
                "new_password": "new-password123",
            },
            format="json",
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_requires_authentication(
        self,
        api_client,
    ):
        response = api_client.post(
            self.endpoint,
            {
                "old_password": "password",
                "new_password": "new-password123",
            },
            format="json",
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
