# backend/contacts/tests/factories.py
import random

import factory
from companies.tests.factories import CompanyFactory
from faker import Faker

from contacts.models import (
    Contact,
    ContactEmail,
    ContactPhone,
    ContactSource,
    ContactTag,
    ContactType,
)

faker = Faker()


class ContactFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Contact

    first_name = factory.Faker("first_name")  # type: ignore
    last_name = factory.Faker("last_name")  # type: ignore
    job_title = factory.Faker("job")  # type: ignore
    email = factory.Sequence(lambda n: f"user{n}@example.com")  # type: ignore
    phone = factory.Faker("phone_number")  # type: ignore
    mobile = factory.Faker("phone_number")  # type: ignore
    contact_type = factory.LazyAttribute(lambda _: random.choice(ContactType.values))  # type: ignore
    source = factory.LazyAttribute(lambda _: random.choice(ContactSource.values))  # type: ignore
    company = factory.SubFactory(CompanyFactory)  # type: ignore
    address = factory.Faker("street_address")  # type: ignore
    city = factory.Faker("city")  # type: ignore
    country = factory.Faker("country")  # type: ignore
    # Nullable FKs — default to None so we don't spin up a User on every company.
    # Override in tests when needed: ContactFactory(owner=some_user)
    owner = None


class ContactTagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ContactTag

    name = factory.Sequence(lambda n: f"Tag {n}")  # type: ignore


class ContactEmailFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ContactEmail

    contact = factory.SubFactory(ContactFactory)  # type: ignore
    email = factory.Faker("email")  # type: ignore
    is_primary = False  # type: ignore


class ContactPhoneFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ContactPhone

    contact = factory.SubFactory(ContactFactory)  # type: ignore
    phone = factory.Faker("phone_number")  # type: ignore
    is_primary = False  # type: ignore
