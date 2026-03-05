from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.requests import Request

from src.app.services.http import create_http_client



def get_client (request: Request):
    return request.app.state.http_client
