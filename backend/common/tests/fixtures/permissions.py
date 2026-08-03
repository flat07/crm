import pytest
from staff.tests.factories import DepartmentFactory, PermissionFactory, RoleFactory


@pytest.fixture
def permissions():
    def create(*codes):
        return [
            PermissionFactory(
                code=code,
                name=code,
            )
            for code in codes
        ]

    return create


@pytest.fixture
def department():
    return DepartmentFactory()


@pytest.fixture
def permission():
    return PermissionFactory()


@pytest.fixture
def user_with_custom_permissions(user, permissions):
    def _create_user_with_perms(*perm_strings):
        perms = permissions(*perm_strings)
        role = RoleFactory()
        role.permissions.add(*perms)
        user.roles.add(role)
        return user

    return _create_user_with_perms


@pytest.fixture
def auth_client_no_permissions(api_client, user):
    response = api_client.post(
        "/api/v1/staff/auth/login/",
        {
            "email": user.email,
            "password": "password",
        },
    )

    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {response.data['access']}")

    return api_client
