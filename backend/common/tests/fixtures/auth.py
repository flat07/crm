import pytest


@pytest.fixture
def auth_client(api_client, user):
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def auth_admin(api_client, administrator):
    api_client.force_authenticate(user=administrator)
    return api_client
