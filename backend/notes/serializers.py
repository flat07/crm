# backend/notes/serializers.py

from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from .models import Note

CONTENT_TYPE_MAP = {
    "company": "companies.company",
    "contact": "contacts.contact",
    "lead": "leads.lead",
    "deal": "deals.deal",
}


class NoteListSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(
        source="created_by.get_full_name",
        read_only=True,
    )

    content_type = serializers.SerializerMethodField()
    object_display = serializers.SerializerMethodField()

    class Meta:
        model = Note
        fields = (
            "id",
            "title",
            "content",
            "content_type",
            "object_id",
            "object_display",
            "created_by",
            "created_by_name",
            "is_pinned",
            "is_private",
            "created_at",
            "updated_at",
        )

    def get_content_type(self, obj):
        return obj.content_type.model

    def get_object_display(self, obj):
        if not obj.content_object:
            return None

        return str(obj.content_object)


class ContentTypeField(serializers.CharField):
    def to_representation(self, value):
        return value.model


class NoteDetailSerializer(serializers.ModelSerializer):
    content_type = ContentTypeField()

    created_by = serializers.UUIDField(
        source="created_by.id",
        read_only=True,
    )

    content_object = serializers.SerializerMethodField(
        read_only=True,
    )

    class Meta:
        model = Note
        fields = (
            "id",
            "title",
            "content",
            "created_by",
            "is_pinned",
            "is_private",
            "content_type",
            "object_id",
            "content_object",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "created_by",
            "content_object",
            "created_at",
            "updated_at",
        )

    def validate_content_type(self, value):
        value = value.lower()

        if value not in CONTENT_TYPE_MAP:
            raise serializers.ValidationError(f"Unsupported content type: {value}.")

        app_label, model = CONTENT_TYPE_MAP[value].split(".")

        try:
            ContentType.objects.get(
                app_label=app_label,
                model=model,
            )
        except ContentType.DoesNotExist:
            raise serializers.ValidationError(f"Content type '{value}' does not exist.")

        return value

    def validate(self, attrs):
        content_type_name = attrs.get("content_type")
        object_id = attrs.get("object_id")

        if not content_type_name or not object_id:
            return attrs

        app_label, model = CONTENT_TYPE_MAP[content_type_name].split(".")

        content_type = ContentType.objects.get(
            app_label=app_label,
            model=model,
        )

        model_class = content_type.model_class()

        if not model_class.objects.filter(  # type: ignore
            pk=object_id,
        ).exists():
            raise serializers.ValidationError(
                {"object_id": (f"{content_type_name.capitalize()} does not exist.")}
            )

        return attrs

    # def create(self, validated_data):
    #     content_type_name = validated_data.pop("content_type")

    #     app_label, model = CONTENT_TYPE_MAP[content_type_name].split(".")

    #     content_type = ContentType.objects.get(
    #         app_label=app_label,
    #         model=model,
    #     )

    #     validated_data["content_type"] = content_type

    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     content_type_name = validated_data.pop(
    #         "content_type",
    #         None,
    #     )

    #     if content_type_name:
    #         app_label, model = CONTENT_TYPE_MAP[content_type_name].split(".")

    #         validated_data["content_type"] = ContentType.objects.get(
    #             app_label=app_label,
    #             model=model,
    #         )

    #     return super().update(
    #         instance,
    #         validated_data,
    #     )

    def get_content_object(self, obj):
        if not obj.content_object:
            return None

        return {
            "id": str(obj.content_object.pk),
            "type": obj.content_type.model,
            "display": str(obj.content_object),
        }


NoteSerializer = NoteDetailSerializer
