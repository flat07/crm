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
        "login/",
        LoginView.as_view(),
        name="login",
    ),
    path(
        "refresh/",
        TokenRefreshView.as_view(),
        name="refresh",
    ),
    path(
        "logout/",
        LogoutView.as_view(),
        name="logout",
    ),
    path(
        "me/",
        MeView.as_view(),
        name="me",
    ),
    path(
        "change-password/",
        ChangePasswordView.as_view(),
        name="change-password",
    ),
]

urlpatterns += router.urls

# /api/v1/auth/users/
# /api/v1/auth/auth/change-password/
# /api/v1/auth/auth/me/
# /api/v1/auth/auth/refresh/
# /api/v1/auth/auth/logout/
# /api/v1/auth/auth/login/
# {
#   "refresh": "",
#   "access": ""
# }
