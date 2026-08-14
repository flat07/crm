# backend/activities/serializers.py

from rest_framework import serializers
from staff.models import User
from staff.serializers import StaffBriefSerializer

from .models import Activity


class ContentTypeField(serializers.CharField):
    def to_representation(self, value):
        if not value:
            return None

        return value.model

    def to_internal_value(self, data):
        return super().to_internal_value(data).lower().strip()


CONTENT_TYPE_MAP = {
    "contact": ("contacts", "contact"),
    "company": ("companies", "company"),
    "lead": ("leads", "lead"),
    "deal": ("deals", "deal"),
}


class ActivitySerializer(serializers.ModelSerializer):
    owner = StaffBriefSerializer(read_only=True)

    owner_id = serializers.PrimaryKeyRelatedField(
        source="owner",
        queryset=User.objects.all(),
        write_only=True,
        required=False,
        allow_null=True,
    )

    owner_name = serializers.SerializerMethodField()

    content_type = ContentTypeField()

    content_type_name = serializers.SerializerMethodField(
        read_only=True,
    )

    content_object_name = serializers.SerializerMethodField(
        read_only=True,
    )

    class Meta:
        model = Activity

        fields = (
            "id",
            "title",
            "description",
            "activity_type",
            "status",
            "priority",
            "due_date",
            "completed_at",
            "owner",
            "owner_id",
            "owner_name",
            "created_by",
            "content_type",
            "content_type_name",
            "object_id",
            "content_object_name",
            "is_active",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "created_by",
            "content_type_name",
            "content_object_name",
            "created_at",
            "updated_at",
        )

    def get_owner_name(self, obj):
        if not obj.owner:
            return None

        return obj.owner.get_full_name()

    def get_content_type_name(self, obj):
        if not obj.content_type:
            return None

        return obj.content_type.model

    def get_content_object_name(self, obj):
        if not obj.content_object:
            return None

        content_type = obj.content_type.model
        content_object = obj.content_object

        if content_type == "contact":
            return content_object.full_name

        if content_type == "company":
            return content_object.name

        if content_type == "lead":
            return content_object.title

        if content_type == "deal":
            return (
                content_object.company.name
                if content_object.company
                else str(content_object)
            )

        return str(content_object)

    def validate_content_type(self, value):
        value = value.lower().strip()

        if value not in CONTENT_TYPE_MAP:
            raise serializers.ValidationError("Invalid content type.")

        return value
