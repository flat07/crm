# backend/common/exceptions.py


class CRMException(Exception):
    pass


class DomainError(Exception):
    """
    Base exception for all business rule violations.
    """

    status_code = 400

    default_message = "A domain error occurred."

    def __init__(
        self,
        message=None,
    ):
        self.message = message or self.default_message

        super().__init__(self.message)
