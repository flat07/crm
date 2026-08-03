# backend/companies/api/views.py
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import decorators, response, status, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated

from companies import selectors, services
from companies.filters import CompanyFilter
from companies.permissions import (
    CanCreateCompany,
    CanDeleteCompany,
    CanUpdateCompany,
    CanViewCompany,
)
from companies.serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer

    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )

    filterset_class = CompanyFilter

    search_fields = (
        "name",
        "legal_name",
        "email",
        "phone",
        "website",
    )

    ordering_fields = (
        "name",
        "created_at",
        "updated_at",
    )

    ordering = ("name",)
    permission_classes = (IsAuthenticated,)

    permission_classes_by_action = {  # noqa: RUF012
        "list": (CanViewCompany,),
        "retrieve": (CanViewCompany,),
        "create": (CanCreateCompany,),
        "update": (CanUpdateCompany,),
        "partial_update": (CanUpdateCompany,),
        "destroy": (CanDeleteCompany,),
        "restore": (CanDeleteCompany,),
        "hard_delete": (CanDeleteCompany,),
    }

    def get_permissions(self):
        permission_classes = self.permission_classes_by_action.get(
            self.action,
            self.permission_classes,
        )
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        return selectors.company_list()

    def perform_create(self, serializer):
        serializer.instance = services.create(
            created_by=self.request.user,
            **serializer.validated_data,
        )

    def perform_update(self, serializer):
        serializer.instance = services.update(
            company=self.get_object(),
            **serializer.validated_data,
        )

    def perform_destroy(self, instance):
        services.archive(
            company=instance,
        )

    @decorators.action(
        detail=True,
        methods=["post"],
    )
    def restore(self, request, pk=None):
        company = self.get_object()

        services.restore(
            company=company,
        )

        return response.Response(
            self.get_serializer(company).data,
            status=status.HTTP_200_OK,
        )

    @decorators.action(
        detail=True,
        methods=["delete"],
    )
    def hard_delete(self, request, pk=None):
        company = self.get_object()

        services.delete(
            company=company,
        )

        return response.Response(
            status=status.HTTP_204_NO_CONTENT,
        )
