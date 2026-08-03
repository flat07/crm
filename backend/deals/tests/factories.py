# backend/deals/tests/factories.py
import random

import factory
from companies.tests.factories import CompanyFactory
from faker import Faker

from deals.models import Deal, DealStage

faker = Faker()

from leads.tests.factories import LeadFactory  # Ensure this import path exists


class DealFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Deal

    # Unique 1-to-1 relationship requires a SubFactory
    lead = factory.SubFactory(LeadFactory)  # type: ignore

    # Required ForeignKey
    company = factory.SubFactory(CompanyFactory)  # type: ignore

    # Model fields
    stage = factory.Iterator(DealStage.values)  # type: ignore
    amount = factory.Faker("pydecimal", left_digits=5, right_digits=2, positive=True)  # type: ignore
    probability = factory.LazyAttribute(lambda _: random.randint(0, 100))  # type: ignore
    description = factory.Faker("paragraph")  # type: ignore

    # Dates
    expected_close_date = factory.Faker("future_date")  # type: ignore
    actual_close_date = None

    # Nullable ForeignKeys set to None to keep setups lightweight
    contact = None
    owner = None
