# backend/notes/factories.py

import factory
from companies.tests.factories import CompanyFactory
from django.contrib.contenttypes.models import ContentType
from staff.tests.factories import UserFactory

from notes.models import Note


class NoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Note

    title = factory.Faker("sentence", nb_words=4)  # type: ignore
    content = factory.Faker("paragraph")  # type: ignore

    created_by = factory.SubFactory(UserFactory)  # type: ignore

    is_pinned = False
    is_private = False

    content_type = factory.LazyAttribute(  # type: ignore
        lambda obj: ContentType.objects.get_for_model(CompanyFactory._meta.model)
    )

    object_id = factory.LazyAttribute(lambda obj: CompanyFactory.create().id)  # type: ignore
