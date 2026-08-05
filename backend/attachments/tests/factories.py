# backend/tests/factories/attachment.py

from __future__ import annotations

import factory
from companies.tests.factories import CompanyFactory
from django.contrib.contenttypes.models import ContentType
from staff.tests.factories import UserFactory

from attachments.models import Attachment


class AttachmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Attachment
        skip_postgeneration_save = True

    file = factory.django.FileField(
        filename="document.txt",
        data=b"Hello, World!",
    )

    filename = factory.LazyAttribute(  # type: ignore
        lambda obj: obj.file.name.split("/")[-1]
    )

    description = factory.Faker("sentence")  # type: ignore

    mime_type = "text/plain"

    file_size = factory.LazyAttribute(  # type: ignore
        lambda obj: obj.file.size
    )

    uploaded_by = factory.SubFactory(UserFactory)  # type: ignore

    content_type = factory.LazyFunction(  # type: ignore
        lambda: ContentType.objects.get_for_model(Attachment)
    )

    object_id = factory.Faker("uuid4")  # type: ignore

    @factory.post_generation  # type: ignore
    def content_object(self, create, extracted, **kwargs):
        if not create:
            return

        obj = extracted or CompanyFactory()

        self.content_type = ContentType.objects.get_for_model(obj)
        self.object_id = obj.pk
        self.save()  # type: ignore
