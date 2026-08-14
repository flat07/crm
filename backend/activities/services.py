# backend/activities/services.py

from django.contrib.contenttypes.models import ContentType
from django.db import transaction

from .models import Activity
from .serializers import CONTENT_TYPE_MAP


@transaction.atomic
def update_activity(
    *,
    activity,
    **validated_data,
):
    content_type_name = validated_data.pop(
        "content_type",
        None,
    )

    if content_type_name is not None:
        app_label, model = CONTENT_TYPE_MAP[content_type_name]

        validated_data["content_type"] = ContentType.objects.get(
            app_label=app_label,
            model=model,
        )

    for field, value in validated_data.items():
        setattr(activity, field, value)

    activity.save()

    return activity


@transaction.atomic
def create_activity(
    *,
    content_type,
    object_id,
    **validated_data,
):
    app_label, model = CONTENT_TYPE_MAP[content_type]

    content_type = ContentType.objects.get(
        app_label=app_label,
        model=model,
    )

    activity = Activity.objects.create(
        content_type=content_type,
        object_id=object_id,
        **validated_data,
    )

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
