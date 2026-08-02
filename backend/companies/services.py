# backend/companies/services.py

from django.db import transaction

from .models import Company


@transaction.atomic
def create(*, created_by, **data) -> Company:
    return Company.objects.create(
        created_by=created_by,
        **data,
    )


@transaction.atomic
def update(*, company: Company, **data) -> Company:
    for field, value in data.items():
        setattr(company, field, value)

    company.save()

    return company


@transaction.atomic
def archive(*, company: Company) -> Company:
    company.soft_delete()
    return company


@transaction.atomic
def restore(*, company: Company) -> Company:
    company.restore()
    return company


@transaction.atomic
def delete(*, company: Company) -> None:
    company.delete()
