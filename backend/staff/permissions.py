from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(
        self,
        request,
        view,
    ):
        return request.user.is_superuser


class IsAuthenticatedUser(BasePermission):
    def has_permission(
        self,
        request,
        view,
    ):
        return request.user.is_authenticated


class HasPermission(BasePermission):
    permission_code = None

    def has_permission(
        self,
        request,
        view,
    ):

        if not request.user.is_authenticated:
            return False

        if request.user.is_superuser:
            return True

        return request.user.has_permission(
            self.permission_code,
        )
