# backend/staff/auth_views.py
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import (
    ChangePasswordSerializer,
    LoginSerializer,
    UserDetailSerializer,
)


# backend/staff/auth_views.py
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):

        refresh = request.data.get("refresh")

        if not refresh:
            return Response(
                {"detail": "Refresh token required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        token = RefreshToken(
            refresh,
        )

        token.blacklist()

        return Response(
            status=status.HTTP_205_RESET_CONTENT,
        )


class MeView(
    RetrieveUpdateAPIView,
):
    serializer_class = UserDetailSerializer

    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class ChangePasswordView(APIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = ChangePasswordSerializer

    def post(
        self,
        request,
    ):

        serializer = self.serializer_class(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        user = request.user

        if not user.check_password(serializer.validated_data["old_password"]):  # type: ignore
            return Response(
                {"old_password": ["Incorrect password."]},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user.set_password(serializer.validated_data["new_password"])  # type: ignore

        user.save()

        return Response({"detail": "Password changed successfully."})
