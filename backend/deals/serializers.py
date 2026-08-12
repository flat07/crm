# backend/deals/serializers.py

from companies.models import Company
from contacts.models import Contact
from leads.models import Lead
from rest_framework import serializers
from staff.models import User

from .models import Deal


class StaffBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
        )


class LeadBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = (
            "id",
            "title",
        )


class ContactBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            "id",
            "first_name",
            "last_name",
        )


class CompanyBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            "id",
            "name",
        )


class DealSerializer(serializers.ModelSerializer):
    lead = LeadBriefSerializer(read_only=True)
    company = CompanyBriefSerializer(read_only=True)
    contact = ContactBriefSerializer(read_only=True)
    owner = StaffBriefSerializer(read_only=True)

    lead_id = serializers.PrimaryKeyRelatedField(
        source="lead",
        queryset=Lead.objects.all(),
        write_only=True,
        required=False,
        allow_null=True,
    )

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
        model = Deal

        fields = (
            "id",
            "lead",
            "lead_id",
            "company",
            "company_id",
            "company_name",
            "contact",
            "contact_id",
            "contact_name",
            "owner",
            "owner_id",
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
