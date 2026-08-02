from .models import User


def user_list():
    return User.objects.select_related(
        "department",
    ).prefetch_related(
        "roles",
    )


def user_detail(user_id):
    return (
        User.objects.select_related(
            "department",
        )
        .prefetch_related(
            "roles",
        )
        .get(
            pk=user_id,
        )
    )
