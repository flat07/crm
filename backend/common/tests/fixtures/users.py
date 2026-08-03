import pytest
from staff.tests.factories import UserFactory


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
