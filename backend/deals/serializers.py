# backend/deals/serializers.py

from rest_framework import serializers

from .models import Deal


class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal

        fields = (
            "id",
            "lead",
            "company",
            "contact",
            "owner",
            "stage",
            "amount",
            "probability",
            "expected_close_date",
            "actual_close_date",
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
        from .services import create_deal

        return create_deal(**validated_data)

    def update(
        self,
        instance,
        validated_data,
    ):
        from .services import update_deal

        return update_deal(
            deal=instance,
            **validated_data,
        )
