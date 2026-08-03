# backend/deals/permissions.py
from staff.permissions import HasPermission


class CanViewDeal(
    HasPermission,
):
    permission_code = "deal.view"


class CanCreateDeal(
    HasPermission,
):
    permission_code = "deal.create"


class CanUpdateDeal(
    HasPermission,
):
    permission_code = "deal.update"


class CanDeleteDeal(
    HasPermission,
):
    permission_code = "deal.delete"
