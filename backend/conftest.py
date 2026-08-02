# tests/conftest.py

import pytest
from rest_framework.test import APIClient
from staff.tests.factories import (
    DepartmentFactory,
    PermissionFactory,
    RoleFactory,
    UserFactory,
)


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def auth_client(api_client, administrator):
    api_client.force_authenticate(user=administrator)
    return api_client


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


@pytest.fixture
def auth_client_with_company_permissions(
    api_client,
    user_with_company_permissions,
):
    response = api_client.post(
        "/api/v1/staff/auth/login/",
        {
            "email": user_with_company_permissions.email,
            "password": "password",
        },
    )

    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {response.data['access']}")

    return api_client


@pytest.fixture
def user_with_company_permissions(user):
    permissions = [
        PermissionFactory(code="company.view"),
        PermissionFactory(code="company.create"),
        PermissionFactory(code="company.update"),
        PermissionFactory(code="company.delete"),
    ]

    role = RoleFactory()

    role.permissions.add(*permissions)

    user.roles.add(role)

    return user


@pytest.fixture
def department():
    return DepartmentFactory()


@pytest.fixture
def permission():
    return PermissionFactory()


@pytest.fixture
def role():
    return RoleFactory()


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def admin_user():
    return UserFactory(
        email="admin@example.com",
        is_superuser=True,
    )


@pytest.fixture
def administrator_role():
    return RoleFactory(name="Administrator")


@pytest.fixture
def sales_manager_role():
    return RoleFactory(name="Sales Manager")


@pytest.fixture
def support_role():
    return RoleFactory(name="Support")


@pytest.fixture
def company_view_permission():
    return PermissionFactory(
        code="company.view",
        name="View Company",
    )


@pytest.fixture
def company_create_permission():
    return PermissionFactory(
        code="company.create",
        name="Create Company",
    )


@pytest.fixture
def administrator(
    administrator_role,
):
    return UserFactory(
        email="admin@example.com",
        is_superuser=True,
        roles=[administrator_role],
    )


@pytest.fixture
def sales_manager(
    sales_manager_role,
    department,
):
    return UserFactory(
        email="manager@example.com",
        department=department,
        roles=[sales_manager_role],
    )
