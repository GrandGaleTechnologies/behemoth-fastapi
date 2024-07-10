from contextlib import asynccontextmanager

from anyio import to_thread
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import ORJSONResponse
from sqlalchemy.orm import Session

from app.core.dependencies import get_session


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
        "email": "angobello0@gmail.com",
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


# Healthcheck
@app.get("/health")
async def health(_: Session = Depends(get_session)):
    """App Healthcheck"""
    return {"status": "Ok!"}
