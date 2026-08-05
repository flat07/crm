# backend/attachments/filters.py

from django_filters import rest_framework as filters

from attachments.models import Attachment


class AttachmentFilter(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Attachment

        fields = (
            "uploaded_by",
            "content_type",
            "object_id",
            "created_at",
        )
