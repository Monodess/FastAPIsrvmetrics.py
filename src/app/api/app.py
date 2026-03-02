from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.app.api.routers.metrics import router
from src.app.api.utils import lifespan
from src.app.services.http import create_http_client


def get_app():
    app = FastAPI(lifespan=lifespan)
    app.include_router(router)
    return app




