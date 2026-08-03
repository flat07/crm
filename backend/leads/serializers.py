# backend/leads/serializers.py

from rest_framework import serializers

from .models import Lead


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead

        fields = (
            "id",
            "title",
            "company",
            "contact",
            "source",
            "status",
            "estimated_value",
            "probability",
            "expected_close_date",
            "owner",
            "description",
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
        from .services import create_lead

        return create_lead(**validated_data)

    def update(self, instance, validated_data):
        from .services import update_lead

        return update_lead(
            lead=instance,
            **validated_data,
        )
