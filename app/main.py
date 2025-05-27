from contextlib import asynccontextmanager

import logfire
from anyio import to_thread
from fastapi import Depends, FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import ORJSONResponse
from sqlalchemy.orm import Session

from app.common.dependencies import get_session
from app.common.exceptions import (
    BadGatewayError,
    CustomHTTPException,
    InternalServerError,
)
from app.core.handlers import (
    bad_gateway_error_exception_handler,
    base_exception_handler,
    custom_http_exception_handler,
    internal_server_error_exception_handler,
    request_validation_exception_handler,
)
from app.core.settings import get_settings
from app.core.tags import RouteTags
from app.sample_module.apis import router as sample_router

# Globals
tags = RouteTags()
settings = get_settings()


# Lifespan (startup, shutdown)
@asynccontextmanager
async def lifespan(_: FastAPI):
    """This is the startup and shutdown code for the FastAPI application."""
    # Startup code
    print("Starting Server...")

    # Bigger Threadpool i.e you send a bunch of requests it will handle a max of 1000 at a time, the default is 40 # pylint: disable=line-too-long
    limiter = to_thread.current_default_thread_limiter()
    limiter.total_tokens = 1000

    # Shutdown Code
    yield
    print("Shutting Down Server...")


app = FastAPI(
    title="Behemoth FastAPI",
    lifespan=lifespan,
    default_response_class=ORJSONResponse,
    docs_url="/",
    contact={
        "name": "GrandGale Technologies",
        "url": "https://github.com/GrandGaleTechnologies",
        "email": "contact@grandgale.tech",
    },
)

# Allowed Origins
origins = ["*"]

# Middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(
    GZipMiddleware,
    minimum_size=5000,  # Minimum size of the response before it is compressed in bytes
)


# Exception Handlers
app.add_exception_handler(Exception, base_exception_handler)
app.add_exception_handler(RequestValidationError, request_validation_exception_handler)  # type: ignore
app.add_exception_handler(InternalServerError, internal_server_error_exception_handler)  # type: ignore
app.add_exception_handler(BadGatewayError, bad_gateway_error_exception_handler)  # type: ignore
app.add_exception_handler(CustomHTTPException, custom_http_exception_handler)  # type: ignore


# Logfire Config
if settings.LOGFIRE_TOKEN:
    logfire.configure(
        token=settings.LOGFIRE_TOKEN, environment="dev" if settings.DEBUG else "prod"
    )
    logfire.instrument_fastapi(app)
    logfire.instrument_asyncpg()


# Healthcheck
@app.get("/health", include_in_schema=False)
async def health(_: Session = Depends(get_session)):
    """App Healthcheck"""
    return {"status": "Ok!"}


# Routers
app.include_router(sample_router, tags=[tags.SAMPLE])
