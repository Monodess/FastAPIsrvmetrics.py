from fastapi import FastAPI, APIRouter
from starlette.routing import Router

from src.app.api.app import get_app
from src.app.api.routers.metrics import router

app = get_app()

"""Root handler"""
@app.get("/")
def read_root():
    return {"Hello": "This is main metrics page"}

app.add_route(router)
