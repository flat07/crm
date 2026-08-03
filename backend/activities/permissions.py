# backend/activities/permissions.py
from staff.permissions import HasPermission


class CanViewActivity(
    HasPermission,
):
    permission_code = "activity.view"


class CanCreateActivity(
    HasPermission,
):
    permission_code = "activity.create"


class CanUpdateActivity(
    HasPermission,
):
    permission_code = "activity.update"


class CanDeleteActivity(
    HasPermission,
):
    permission_code = "activity.delete"
