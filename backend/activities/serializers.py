# backend/activities/serializers.py

from rest_framework import serializers

from .models import Activity


class ActivitySerializer(serializers.ModelSerializer):
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
            "created_by",
            "content_type",
            "object_id",
            "is_active",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )

    def create(self, validated_data):
        from .services import create_activity

        return create_activity(**validated_data)

    def update(
        self,
        instance,
        validated_data,
    ):
        from .services import update_activity

        return update_activity(
            activity=instance,
            **validated_data,
        )
