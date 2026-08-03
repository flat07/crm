# tests/conftest.py

pytest_plugins = (
    "common.tests.fixtures.api",
    "common.tests.fixtures.auth",
    "common.tests.fixtures.users",
    "common.tests.fixtures.roles",
    "common.tests.fixtures.permissions",
    "contacts.tests.fixtures",
    "companies.tests.fixtures",
    "deals.tests.fixtures",
    "leads.tests.fixtures",
    "activities.tests.fixtures",
)
