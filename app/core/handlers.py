from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import ORJSONResponse

from app.common.exceptions import (
    BadGatewayError,
    CustomHTTPException,
    InternalServerError,
)
from app.core.settings import get_settings

# Globals
settings = get_settings()


async def base_exception_handler(_: Request, exc: Exception):
    """
    Exception handler for general Exception
    """
    # Send email to staff
    if settings.DEBUG:
        print(exc)
    else:
        # Send email to staff
        # sendgrid.send_email()
        ...

    return ORJSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=jsonable_encoder(
            {
                "status": "error",
                "error": {"msg": "Internal Server Error", "loc": []},
                "data": None,
            }
        ),
    )


async def request_validation_exception_handler(_: Request, exc: RequestValidationError):
    """
    Exception handler for 'RequestValidationError' raised by pydantic
    """

    # Get error message
    error = exc.errors()[0]

    return ORJSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(
            {
                "status": "error",
                "error": {"msg": error["msg"], "loc": error["loc"]},
                "data": None,
            }
        ),
    )


async def internal_server_error_exception_handler(_: Request, exc: InternalServerError):
    """
    Exception handler for 'InternalServerError' exception
    """
    # Send email to staff
    if settings.DEBUG:
        print(exc)
    else:
        # Send staff a notice
        # sendgrid.send_email()
        ...

    return ORJSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=jsonable_encoder(
            {
                "status": "error",
                "error": {"msg": "Internal Server Error", "loc": []},
                "data": None,
            }
        ),
    )


async def bad_gateway_error_exception_handler(_: Request, exc: BadGatewayError):
    """
    Exception handler for 'BadGatewayError' exception
    """
    if settings.DEBUG:
        print(exc)
    else:
        # Send email to staff
        # sendgrid.send_email()
        ...

    return ORJSONResponse(
        status_code=status.HTTP_502_BAD_GATEWAY,
        content=jsonable_encoder(
            {
                "status": "error",
                "error": {"msg": "Bad Gateway Please Contact Support", "loc": exc.loc},
                "data": None,
            }
        ),
    )


async def custom_http_exception_handler(_: Request, exc: CustomHTTPException):
    """
    Exception handler for 'NotFound' exception
    """
    return ORJSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder(
            {
                "status": "error",
                "error": {"msg": exc.msg, "loc": exc.loc},
                "data": None,
            }
        ),
    )
