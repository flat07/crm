# backend/attachments/serializers.py

from rest_framework import serializers

from attachments.models import Attachment


class AttachmentSerializer(serializers.ModelSerializer):
    uploaded_by_email = serializers.EmailField(
        source="uploaded_by.email",
        read_only=True,
    )

    class Meta:
        model = Attachment

        fields = (
            "id",
            "file",
            "filename",
            "description",
            "mime_type",
            "file_size",
            "uploaded_by",
            "uploaded_by_email",
            "content_type",
            "object_id",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "filename",
            "mime_type",
            "file_size",
            "uploaded_by",
            "created_at",
            "updated_at",
        )
