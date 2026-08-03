# backend/activities/services.py

from django.db import transaction

from .models import Activity


@transaction.atomic
def create_activity(**validated_data) -> Activity:
    return Activity.objects.create(**validated_data)


@transaction.atomic
def update_activity(
    *,
    activity: Activity,
    **validated_data,
) -> Activity:
    for field, value in validated_data.items():
        setattr(activity, field, value)

    activity.save()

    return activity


@transaction.atomic
def archive(*, activity: Activity) -> Activity:
    activity.soft_delete()
    return activity


@transaction.atomic
def restore(*, activity: Activity) -> Activity:
    activity.restore()
    return activity


@transaction.atomic
def delete_activity(activity: Activity) -> None:
    activity.delete()
