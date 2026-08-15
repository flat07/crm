# backend/notes/permissions.py
from staff.permissions import HasPermission


class CanViewNote(
    HasPermission,
):
    permission_code = "note.view"


class CanCreateNote(
    HasPermission,
):
    permission_code = "note.create"


class CanUpdateNote(
    HasPermission,
):
    permission_code = "note.update"


class CanDeleteNote(
    HasPermission,
):
    permission_code = "note.delete"
