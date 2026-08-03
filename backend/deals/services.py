# backend/deals/services.py

from django.db import transaction

from .models import Deal


@transaction.atomic
def create_deal(**validated_data) -> Deal:
    return Deal.objects.create(**validated_data)


@transaction.atomic
def update_deal(
    *,
    deal: Deal,
    **validated_data,
) -> Deal:
    for field, value in validated_data.items():
        setattr(deal, field, value)

    deal.save()

    return deal


@transaction.atomic
def archive(*, deal: Deal) -> Deal:
    deal.soft_delete()
    return deal


@transaction.atomic
def restore(*, deal: Deal) -> Deal:
    deal.restore()
    return deal


@transaction.atomic
def delete_deal(deal: Deal) -> None:
    deal.delete()
