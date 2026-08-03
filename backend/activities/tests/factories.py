# backend/activities/tests/factories.py

import factory
from companies.tests.factories import CompanyFactory
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from factory.django import DjangoModelFactory
from staff.tests.factories import UserFactory

from activities.models import (
    Activity,
    ActivityPriority,
    ActivityStatus,
    ActivityType,
)


class ActivityFactory(DjangoModelFactory):
    class Meta:
        model = Activity
        skip_postgeneration_save = True

    title = factory.Faker("sentence", nb_words=4)  # type: ignore
    description = factory.Faker("paragraph")  # type: ignore

    activity_type = ActivityType.CALL
    status = ActivityStatus.PLANNED
    priority = ActivityPriority.MEDIUM

    due_date = factory.LazyFunction(lambda: timezone.now() + timezone.timedelta(days=3))  # type: ignore

    completed_at = None

    owner = factory.SubFactory(UserFactory)  # type: ignore
    created_by = factory.SubFactory(UserFactory)  # type: ignore

    #
    # Default generic relation.
    # Can be overridden by passing content_object=...
    #
    content_type = factory.LazyAttribute(  # type: ignore
        lambda _: ContentType.objects.get_for_model(CompanyFactory._meta.model)
    )

    object_id = factory.LazyAttribute(lambda _: CompanyFactory().pk)  # type: ignore

    @factory.post_generation  # type: ignore
    def content_object(self, create, extracted, **kwargs):
        """
        Usage:

            ActivityFactory(content_object=lead)
            ActivityFactory(content_object=deal)
            ActivityFactory(content_object=contact)
        """

        if extracted is None:
            return

        self.content_type = ContentType.objects.get_for_model(extracted)
        self.object_id = extracted.pk

        if create:
            self.save(update_fields=["content_type", "object_id"])  # type: ignore
