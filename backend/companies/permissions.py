# backend/companies/permissions.py
from staff.permissions import HasPermission


class CanViewCompany(
    HasPermission,
):
    permission_code = "company.view"


class CanCreateCompany(
    HasPermission,
):
    permission_code = "company.create"


class CanUpdateCompany(
    HasPermission,
):
    permission_code = "company.update"


class CanDeleteCompany(
    HasPermission,
):
    permission_code = "company.delete"
