from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import ORJSONResponse

from app.common.exceptions import NotFound


async def base_exception_handler(_: Request, exc: Exception):
    """
    Exception handler for 'NotFound' exception
    """
    # Send email to staff
    # sendgrid.send_email()
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


async def not_found_exception_handler(_: Request, exc: NotFound):
    """
    Exception handler for 'NotFound' exception
    """
    return ORJSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(
            {
                "status": "error",
                "error": {"msg": exc.msg, "loc": exc.loc},
                "data": None,
            }
        ),
    )
