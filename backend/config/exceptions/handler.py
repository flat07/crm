# backend/config/exceptions/handler.py
import logging

from common.exceptions import (
    DomainError,
)
from rest_framework.response import (
    Response,
)
from rest_framework.views import (
    exception_handler,
)

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        return response

    logger.exception("Unhandled exception")

    if isinstance(exc, DomainError):
        return Response(
            {"detail": exc.message},
            status=exc.status_code,
        )

    return Response(
        {"detail": "Internal server error."},
        status=500,
    )
