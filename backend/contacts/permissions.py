# backend/contacts/permissions.py
from staff.permissions import HasPermission


class CanViewContact(
    HasPermission,
):
    permission_code = "contact.view"


class CanCreateContact(
    HasPermission,
):
    permission_code = "contact.create"


class CanUpdateContact(
    HasPermission,
):
    permission_code = "contact.update"


class CanDeleteContact(
    HasPermission,
):
    permission_code = "contact.delete"
