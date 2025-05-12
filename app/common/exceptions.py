from datetime import datetime


class CustomHTTPException(Exception):
    """
    Common base class for all http exceptions
    """

    def __init__(self, msg: str, *, status_code: int, loc: list | None = None):
        self.status_code = status_code
        self.msg = msg
        self.loc = loc

    def __str__(self) -> str:
        return f"Status Code: {self.status_code}\nMessage: {self.msg}\nLocation: {self.loc}"


class InternalServerError(Exception):
    """
    Common base class for all 500 internal server error responses
    """

    def __init__(self, msg: str, *, loc: str):
        self.msg = msg
        self.loc = loc
        self.timestamp = datetime.now()

    def __str__(self) -> str:
        return f"Message: {self.msg}\nLocation: {self.loc}\nTimestamp: {self.timestamp}"


class BadGatewayError(Exception):
    """
    Common base class for all 500 bad gateway error responses
    """

    def __init__(self, msg: str, *, loc: str, service: str):
        self.msg = msg
        self.loc = loc
        self.service = service
        self.timestamp = datetime.now()

    def __str__(self) -> str:
        return f"Message: {self.msg}\nLocation: {self.loc}\nService: {self.service}\nTimestamp: {self.timestamp}"


class BadRequest(CustomHTTPException):
    """
    Common base exception for 400 BAD REQUEST exceptions
    """

    def __init__(self, msg: str, *, loc: list | None = None):
        super().__init__(msg, status_code=400, loc=loc)


class Unauthorized(CustomHTTPException):
    """
    Common base class for 401 UNAUTHORIZED exceptions
    """

    def __init__(self, msg: str, *, loc: list | None = None):
        super().__init__(msg, status_code=401, loc=loc)


class Forbidden(CustomHTTPException):
    """
    Common base class for 403 FORBIDDEN exceptions
    """

    def __init__(self, msg: str = "Forbidden", *, loc: list | None = None):
        super().__init__(msg, status_code=403, loc=loc)


class NotFound(CustomHTTPException):
    """
    Common base class for 404 NOT FOUND exceptions
    """

    def __init__(self, msg: str, *, loc: list | None = None):
        super().__init__(msg, status_code=404, loc=loc)
