# backend/contacts/serializers.py

from rest_framework import serializers

from .models import (
    Contact,
    ContactEmail,
    ContactPhone,
    ContactTag,
    ContactTagAssignment,
)


class ContactSerializer(serializers.ModelSerializer):
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
            "owner",
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
