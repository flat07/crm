# backend/leads/serializers.py

from companies.models import Company
from companies.serializers import CompanyBriefSerializer
from contacts.models import Contact
from contacts.serializers import ContactBriefSerializer
from rest_framework import serializers
from staff.models import User
from staff.serializers import StaffBriefSerializer

from .models import Lead


class LeadBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = (
            "id",
            "title",
        )


class LeadSerializer(serializers.ModelSerializer):
    company = CompanyBriefSerializer(read_only=True)
    contact = ContactBriefSerializer(read_only=True)
    owner = StaffBriefSerializer(read_only=True)

    company_id = serializers.PrimaryKeyRelatedField(
        source="company",
        queryset=Company.objects.all(),
        write_only=True,
        required=False,
        allow_null=True,
    )

    contact_id = serializers.PrimaryKeyRelatedField(
        source="contact",
        queryset=Contact.objects.all(),
        write_only=True,
        required=False,
        allow_null=True,
    )

    owner_id = serializers.PrimaryKeyRelatedField(
        source="owner",
        queryset=User.objects.all(),
        write_only=True,
        required=False,
        allow_null=True,
    )
    company_name = serializers.CharField(
        source="company.name",
        read_only=True,
    )
    contact_name = serializers.SerializerMethodField()
    owner_name = serializers.SerializerMethodField()

    class Meta:
        model = Lead

        fields = (
            "id",
            "title",
            "company",
            "company_id",
            "company_name",
            "contact",
            "contact_id",
            "contact_name",
            "owner",
            "owner_id",
            "owner_name",
            "source",
            "status",
            "estimated_value",
            "probability",
            "expected_close_date",
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
        from .services import create_lead

        return create_lead(**validated_data)

    def update(self, instance, validated_data):
        from .services import update_lead

        return update_lead(
            lead=instance,
            **validated_data,
        )
