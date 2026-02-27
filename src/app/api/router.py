from typing import Type

from fastapi import APIRouter
from oci.waas.models import HealthCheck
from starlette.requests import Request

from src.app.DAL.data_reader import find_by
from src.app.DAL.data_writer import write
from src.app.models.models import PageSpeed
from src.app.scheme.base import Base
from src.app.scheme.contracts import Tables
from src.app.services.capturer import process_url
from src.app.services.parser import parse_both
from src.appsetting.appsettings import appsettings

router = APIRouter(prefix="/metrics", tags=["metrics"])

@router.post("/")
async def capture(request: Request, url: str):

    client = request.app.state.http_client
    data = await process_url(client, url, appsettings.PAGESPEED_API_KEY)
    objects = parse_both(data)
    await write(objects)
    return data

"""TODO: fix this"""
@router.get("/")
def read_db(table: str, **kwargs):
    model = Tables(table)
    return find_by(model, **kwargs)



