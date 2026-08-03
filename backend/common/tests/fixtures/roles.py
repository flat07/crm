import pytest
from staff.tests.factories import RoleFactory


@pytest.fixture
def role():
    return RoleFactory()


@pytest.fixture
def administrator_role():
    return RoleFactory(name="Administrator")


@pytest.fixture
def sales_manager_role():
    return RoleFactory(name="Sales Manager")


@pytest.fixture
def support_role():
    return RoleFactory(name="Support")
