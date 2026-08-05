# tests/conftest.py
import pytest

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
    "attachments.tests.fixtures",
)


@pytest.fixture(autouse=True)
def media_storage(settings, tmp_path):
    settings.STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
            "OPTIONS": {
                "location": tmp_path,
            },
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }
