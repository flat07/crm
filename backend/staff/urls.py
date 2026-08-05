# backend/staff/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from .auth_views import (
    ChangePasswordView,
    LoginView,
    LogoutView,
    MeView,
)
from .views import UserViewSet

router = DefaultRouter()

router.register(
    "users",
    UserViewSet,
    basename="users",
)


urlpatterns = [
    path(
        "auth/login/",
        LoginView.as_view(),
        name="login",
    ),
    path(
        "auth/refresh/",
        TokenRefreshView.as_view(),
        name="refresh",
    ),
    path(
        "auth/logout/",
        LogoutView.as_view(),
        name="logout",
    ),
    path(
        "auth/me/",
        MeView.as_view(),
        name="me",
    ),
    path(
        "auth/change-password/",
        ChangePasswordView.as_view(),
        name="change-password",
    ),
]

urlpatterns += router.urls

# /api/v1/staff/users/
# /api/v1/staff/auth/change-password/
# /api/v1/staff/auth/me/
# /api/v1/staff/auth/refresh/
# /api/v1/staff/auth/logout/
# /api/v1/staff/auth/login/
# {
#   "refresh": "",
#   "access": ""
# }
