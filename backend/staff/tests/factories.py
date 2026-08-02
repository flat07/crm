# backend/staff/tests/factories.py
import factory
from factory.django import DjangoModelFactory

from staff.models import Department


class DepartmentFactory(DjangoModelFactory):
    class Meta:
        model = Department

    name = factory.Sequence(lambda n: f"Department {n}")  # type: ignore
    description = factory.Faker("sentence")  # type: ignore


from staff.models import Permission


class PermissionFactory(DjangoModelFactory):
    class Meta:
        model = Permission

    code = factory.Sequence(lambda n: f"permission.{n}")  # type: ignore
    name = factory.Sequence(lambda n: f"Permission {n}")  # type: ignore
    description = factory.Faker("sentence")  # type: ignore


from staff.models import Role


class RoleFactory(DjangoModelFactory):
    class Meta:
        model = Role

    name = factory.Sequence(lambda n: f"Role {n}")  # type: ignore
    description = factory.Faker("sentence")  # type: ignore


from staff.models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        skip_postgeneration_save = True

    email = factory.Sequence(lambda n: f"user{n}@example.com")  # type: ignore

    first_name = factory.Faker("first_name")  # type: ignore
    last_name = factory.Faker("last_name")  # type: ignore

    phone = factory.Faker("phone_number")  # type: ignore

    job_title = factory.Faker("job")  # type: ignore

    department = factory.SubFactory(DepartmentFactory)  # type: ignore

    is_staff = True
    is_superuser = False

    password = factory.PostGenerationMethodCall(  # type: ignore
        "set_password",
        "password",
    )

    @factory.post_generation  # type: ignore
    def roles(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            self.roles.add(*extracted)  # type: ignore

        self.save()  # type: ignore
