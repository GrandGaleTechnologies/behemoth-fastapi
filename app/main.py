from contextlib import asynccontextmanager

import logfire
from fastapi import Depends, FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import ORJSONResponse
from sqlalchemy.orm import Session
from secure import Secure

# Local imports
from app.api.v1 import auth
from app.common.exceptions import (
    BadGatewayError,
    CustomHTTPException,
    InternalServerError,
)
from app.core.database import get_db
from app.core.handlers import (
    bad_gateway_error_exception_handler,
    base_exception_handler,
    custom_http_exception_handler,
    internal_server_error_exception_handler,
    request_validation_exception_handler,
)
from app.core.settings import get_settings
from app.core.tags import get_tags
from app.sample_module.apis import router as sample_router
from app.api.v1 import admin

app.include_router(admin.router)

# Globals
settings = get_settings()
tags = get_tags()
secure_headers = Secure.with_default_headers()

# Lifespan (startup/shutdown)
@asynccontextmanager
async def lifespan(_: FastAPI):
    print("🚀 Starting Server...")
    yield
    print("🛑 Shutting Down Server...")

# Main app
app = FastAPI(
    title="Behemoth FastAPI",
    lifespan=lifespan,
    default_response_class=ORJSONResponse,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",   # 👈 very important
    contact={
        "name": "GrandGale Technologies",
        "url": "https://github.com/GrandGaleTechnologies",
        "email": "contact@grandgale.tech",
    },
)



# Middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(GZipMiddleware, minimum_size=5000)



# Exception Handlers
app.add_exception_handler(Exception, base_exception_handler)
app.add_exception_handler(RequestValidationError, request_validation_exception_handler)
app.add_exception_handler(InternalServerError, internal_server_error_exception_handler)
app.add_exception_handler(BadGatewayError, bad_gateway_error_exception_handler)
app.add_exception_handler(CustomHTTPException, custom_http_exception_handler)

# Logfire Configuration
if settings.LOGFIRE_TOKEN:
    logfire.configure(
        token=settings.LOGFIRE_TOKEN,
        environment="dev" if settings.DEBUG else "prod"
    )
    logfire.instrument_fastapi(app)
    logfire.instrument_sqlalchemy()

from fastapi.responses import RedirectResponse

# Redirect root "/" -> Swagger docs
@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")


# Healthcheck
@app.get("/health", include_in_schema=False)
async def health(_: Session = Depends(get_db)):
    return {"status": "Ok!"}

# Routers
app.include_router(auth.router)
app.include_router(sample_router, tags=[tags.SAMPLE])
