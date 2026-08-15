import pytest


@pytest.fixture
def auth_client_with_contact_permissions(
    api_client,
    user_with_custom_permissions,
):
    user = user_with_custom_permissions(
        "contact.view",
        "contact.create",
        "contact.update",
        "contact.delete",
    )
    response = api_client.post(
        "/api/v1/auth/login/",
        {
            "email": user.email,
            "password": "password",
        },
    )

    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {response.data['access']}")

    return api_client
