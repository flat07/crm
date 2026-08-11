# backend/deals/serializers.py

from rest_framework import serializers

from .models import Deal


class DealSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(
        source="company.name",
        read_only=True,
    )
    contact_name = serializers.SerializerMethodField()
    owner_name = serializers.SerializerMethodField()

    class Meta:
        model = Deal

        fields = (
            "id",
            "lead",
            "company",
            "company_name",
            "contact",
            "contact_name",
            "owner",
            "owner_name",
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

    def get_contact_name(self, obj):
        if not obj.contact:
            return None

        return obj.contact.full_name

    def get_owner_name(self, obj):
        if not obj.owner:
            return None

        return obj.owner.get_full_name()

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
