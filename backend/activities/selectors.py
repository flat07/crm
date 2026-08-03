# backend/activities/selectors.py

from django.contrib.contenttypes.models import ContentType
from django.db.models import QuerySet

from .models import Activity


def activity_list() -> QuerySet[Activity]:
    return Activity.objects.select_related(
        "owner",
        "created_by",
        "content_type",
    )


def activity_detail(activity_id) -> Activity:
    return activity_list().get(pk=activity_id)


def activity_object(
    *,
    content_type: ContentType,
    object_id,
) -> QuerySet[Activity]:
    return activity_list().filter(
        content_type=content_type,
        object_id=object_id,
    )
