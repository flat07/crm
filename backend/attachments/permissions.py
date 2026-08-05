# backend/attachments/permissions.py
from staff.permissions import HasPermission


class CanViewAttachment(
    HasPermission,
):
    permission_code = "attachment.view"


class CanCreateAttachment(
    HasPermission,
):
    permission_code = "attachment.create"


class CanUpdateAttachment(
    HasPermission,
):
    permission_code = "attachment.update"


class CanDeleteAttachment(
    HasPermission,
):
    permission_code = "attachment.delete"
