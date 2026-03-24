from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.app.core.services.http import create_http_client


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = create_http_client()
    app.state.http_client = client

    yield

    await client.aclose()





