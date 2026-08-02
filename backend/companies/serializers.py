# backend/companies/serializers.py

from rest_framework import serializers

from companies.models import Company


class CompanySerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(
        source="owner.get_full_name",
        read_only=True,
    )

    created_by_name = serializers.CharField(
        source="created_by.get_full_name",
        read_only=True,
    )

    class Meta:
        model = Company

        fields = (
            "id",
            "name",
            "legal_name",
            "website",
            "email",
            "phone",
            "industry",
            "company_type",
            "size",
            "tax_number",
            "description",
            "address",
            "city",
            "country",
            "postal_code",
            "owner",
            "owner_name",
            "created_by",
            "created_by_name",
            "is_active",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "created_by",
            "created_at",
            "updated_at",
        )
