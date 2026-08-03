# backend/leads/services.py

from django.db import transaction

from .models import Lead


@transaction.atomic
def create_lead(**validated_data) -> Lead:
    return Lead.objects.create(**validated_data)


@transaction.atomic
def update_lead(
    *,
    lead: Lead,
    **validated_data,
) -> Lead:
    for field, value in validated_data.items():
        setattr(lead, field, value)

    lead.save()

    return lead


@transaction.atomic
def archive(*, lead: Lead) -> Lead:
    lead.soft_delete()
    return lead


@transaction.atomic
def restore(*, lead: Lead) -> Lead:
    lead.restore()
    return lead


@transaction.atomic
def delete_lead(lead: Lead) -> None:
    lead.delete()
