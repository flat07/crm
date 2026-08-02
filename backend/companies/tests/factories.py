# backend/companies/tests/factories.py
import random

import factory
from faker import Faker

from companies.models import Company, CompanySize, CompanyType, Industry

faker = Faker()


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    name = factory.Sequence(lambda n: f"Company {n}")  # type: ignore
    legal_name = factory.LazyAttribute(lambda obj: f"{obj.name} Ltd.")  # type: ignore
    website = factory.LazyAttribute(  # type: ignore
        lambda obj: f"https://www.{obj.name.lower().replace(' ', '')}.com"
    )
    email = factory.LazyAttribute(  # type: ignore
        lambda obj: f"contact@{obj.name.lower().replace(' ', '')}.com"
    )
    phone = factory.LazyAttribute(lambda _: faker.numerify("+1 ### ### ####"))  # type: ignore
    industry = factory.LazyAttribute(lambda _: random.choice(Industry.values))  # type: ignore
    company_type = factory.LazyAttribute(lambda _: random.choice(CompanyType.values))  # type: ignore
    size = factory.LazyAttribute(lambda _: random.choice(CompanySize.values))  # type: ignore
    tax_number = factory.LazyAttribute(lambda _: faker.ein())  # type: ignore
    description = factory.Faker("paragraph")  # type: ignore
    address = factory.Faker("street_address")  # type: ignore
    city = factory.Faker("city")  # type: ignore
    country = factory.Faker("country")  # type: ignore
    postal_code = factory.LazyAttribute(lambda _: faker.postcode()[:20])  # type: ignore

    # Nullable FKs — default to None so we don't spin up a User on every company.
    # Override in tests when needed: CompanyFactory(owner=some_user)
    owner = None
    created_by = None
