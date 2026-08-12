# backend/contacts/serializers.py

from companies.models import Company
from companies.serializers import CompanyBriefSerializer
from rest_framework import serializers
from staff.models import User
from staff.serializers import StaffBriefSerializer

from .models import (
    Contact,
    ContactEmail,
    ContactPhone,
    ContactTag,
    ContactTagAssignment,
)


class ContactBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            "id",
            "first_name",
            "last_name",
        )


class ContactSerializer(serializers.ModelSerializer):
    company = CompanyBriefSerializer(read_only=True)
    owner = StaffBriefSerializer(read_only=True)
    company_id = serializers.PrimaryKeyRelatedField(
        source="company",
        queryset=Company.objects.all(),
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
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = Contact
        fields = (
            "id",
            "first_name",
            "last_name",
            "full_name",
            "job_title",
            "email",
            "phone",
            "mobile",
            "contact_type",
            "source",
            "company",
            "company_id",
            "company_name",
            "owner",
            "owner_id",
            "notes",
            "birthday",
            "linkedin_url",
            "address",
            "city",
            "country",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
            "full_name",
        )

    def create(self, validated_data):
        from .services import create_contact

        return create_contact(**validated_data)

    def update(self, instance, validated_data):
        from .services import update_contact

        return update_contact(
            contact=instance,
            **validated_data,
        )


class ContactTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactTag
        fields = (
            "id",
            "name",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )


class ContactEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactEmail
        fields = (
            "id",
            "contact",
            "email",
            "is_primary",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )


class ContactPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPhone
        fields = (
            "id",
            "contact",
            "phone",
            "is_primary",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )


class ContactTagAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactTagAssignment
        fields = (
            "id",
            "contact",
            "tag",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )
