# backend/contacts/tests/test_contact_filters.py

import pytest
from companies.tests.factories import CompanyFactory
from rest_framework import status
from staff.tests.factories import UserFactory

from contacts.models import ContactSource, ContactType
from contacts.tests.factories import ContactFactory

pytestmark = pytest.mark.django_db


class TestContactSearch:
    endpoint = "/api/v1/contacts/"

    def test_search_first_name(self, auth_admin):
        ContactFactory(first_name="John")
        ContactFactory(first_name="Jane")

        response = auth_admin.get(
            self.endpoint,
            {"search": "John"},
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["first_name"] == "John"


class TestContactFilterType:
    endpoint = "/api/v1/contacts/"

    def test_filter_contact_type(self, auth_admin):
        ContactFactory(contact_type=ContactType.CUSTOMER)
        ContactFactory(contact_type=ContactType.LEAD)

        response = auth_admin.get(
            self.endpoint,
            {
                "contact_type": ContactType.CUSTOMER,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["contact_type"] == ContactType.CUSTOMER


class TestContactFilterSource:
    endpoint = "/api/v1/contacts/"

    def test_filter_source(self, auth_admin):
        ContactFactory(source=ContactSource.WEBSITE)
        ContactFactory(source=ContactSource.REFERRAL)

        response = auth_admin.get(
            self.endpoint,
            {
                "source": ContactSource.WEBSITE,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["source"] == ContactSource.WEBSITE


class TestContactFilterCompany:
    endpoint = "/api/v1/contacts/"

    def test_filter_company(self, auth_admin):
        company = CompanyFactory()

        ContactFactory(company=company)
        ContactFactory()

        response = auth_admin.get(
            self.endpoint,
            {
                "company": company.id,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1


class TestContactFilterOwner:
    endpoint = "/api/v1/contacts/"

    def test_filter_owner(self, auth_admin):
        owner = UserFactory()

        ContactFactory(owner=owner)
        ContactFactory()

        response = auth_admin.get(
            self.endpoint,
            {
                "owner": owner.id,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1


class TestContactFilterCity:
    endpoint = "/api/v1/contacts/"

    def test_filter_city_case_insensitive(self, auth_admin):
        ContactFactory(city="Tashkent")
        ContactFactory(city="Dubai")

        response = auth_admin.get(
            self.endpoint,
            {
                "city": "tashkent",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["city"] == "Tashkent"


class TestContactFilterCountry:
    endpoint = "/api/v1/contacts/"

    def test_filter_country_case_insensitive(self, auth_admin):
        ContactFactory(country="Uzbekistan")
        ContactFactory(country="UAE")

        response = auth_admin.get(
            self.endpoint,
            {
                "country": "uzbekistan",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1


class TestContactFilterBirthday:
    endpoint = "/api/v1/contacts/"

    def test_filter_birthday_after(self, auth_admin):
        ContactFactory(birthday="1990-01-01")
        ContactFactory(birthday="1980-01-01")

        response = auth_admin.get(
            self.endpoint,
            {
                "birthday_after": "1989-01-01",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1

    def test_filter_birthday_before(self, auth_admin):
        ContactFactory(birthday="1990-01-01")
        ContactFactory(birthday="1980-01-01")

        response = auth_admin.get(
            self.endpoint,
            {
                "birthday_before": "1985-01-01",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1


class TestContactOrdering:
    endpoint = "/api/v1/contacts/"

    def test_order_by_last_name(self, auth_admin):
        ContactFactory(last_name="Zulu")
        ContactFactory(last_name="Alpha")

        response = auth_admin.get(
            self.endpoint,
            {
                "ordering": "last_name",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data["results"][0]["last_name"] == "Alpha"

    def test_order_by_created_desc(self, auth_admin):
        older = ContactFactory()
        newer = ContactFactory()

        response = auth_admin.get(
            self.endpoint,
            {
                "ordering": "-created_at",
            },
        )

        assert response.status_code == status.HTTP_200_OK

        ids = [item["id"] for item in response.data["results"]]

        assert ids.index(str(newer.id)) < ids.index(str(older.id))
