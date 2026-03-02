from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.requests import Request

from src.app.services.http import create_http_client


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = create_http_client()
    app.state.http_client = client

    yield

    await client.aclose()

def get_client (request: Request):
    return request.app.state.http_client
