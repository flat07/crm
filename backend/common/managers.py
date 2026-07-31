# backend/common/managers.py

from django.db import models


class ActiveManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(
                deleted_at__isnull=True,
                is_active=True,
            )
        )


class AllObjectsManager(models.Manager):
    pass
