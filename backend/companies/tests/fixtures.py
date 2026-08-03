import pytest


@pytest.fixture
def auth_client_with_company_permissions(
    api_client,
    user_with_custom_permissions,
):
    user = user_with_custom_permissions(
        "company.view",
        "company.create",
        "company.update",
        "company.delete",
    )
    response = api_client.post(
        "/api/v1/staff/auth/login/",
        {
            "email": user.email,
            "password": "password",
        },
    )

    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {response.data['access']}")

    return api_client
