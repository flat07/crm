from django.contrib.auth import authenticate
from django.db import transaction
from rest_framework.exceptions import AuthenticationFailed

from .models import User


@transaction.atomic
def create_user(
    **data,
):

    password = data.pop(
        "password",
    )

    user = User.objects.create_user(  # type: ignore
        password=password,
        **data,
    )

    return user


@transaction.atomic
def update_user(
    *,
    user,
    **data,
):

    for field, value in data.items():
        setattr(
            user,
            field,
            value,
        )

    user.save()

    return user


def authenticate_user(
    email,
    password,
):

    user = authenticate(
        email=email,
        password=password,
    )

    if not user:
        raise AuthenticationFailed("Invalid credentials.")

    return user
