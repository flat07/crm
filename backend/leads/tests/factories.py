# backend/leads/tests/factories.py
import random

import factory
from companies.tests.factories import CompanyFactory

from leads.models import Lead, LeadSource, LeadStatus


class LeadFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Lead

    # Required CharField & SubFactory
    title = factory.Faker("job")  # type: ignore
    company = factory.SubFactory(CompanyFactory)  # type: ignore

    # Choice fields matching your TextChoices
    source = factory.Iterator(LeadSource.values)  # type: ignore
    status = factory.Iterator(LeadStatus.values)  # type: ignore

    # Numerical fields
    estimated_value = factory.Faker(  # type: ignore
        "pydecimal", left_digits=5, right_digits=2, positive=True
    )
    probability = factory.LazyAttribute(lambda _: random.randint(0, 100))  # type: ignore

    # Dates & Text
    expected_close_date = factory.Faker("future_date")  # type: ignore
    description = factory.Faker("paragraph")  # type: ignore

    # Nullable ForeignKeys set to None to optimize performance and prevent DB bloat
    contact = None
    owner = None
