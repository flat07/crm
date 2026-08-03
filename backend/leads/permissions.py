# backend/leads/permissions.py
from staff.permissions import HasPermission


class CanViewLead(
    HasPermission,
):
    permission_code = "lead.view"


class CanCreateLead(
    HasPermission,
):
    permission_code = "lead.create"


class CanUpdateLead(
    HasPermission,
):
    permission_code = "lead.update"


class CanDeleteLead(
    HasPermission,
):
    permission_code = "lead.delete"
