from typing import Dict, Any, Type

from fastapi import APIRouter, Query, HTTPException
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.annotation import Annotated
from starlette.requests import Request

from src.app.DAL.data_reader import find_by
from src.app.DAL.data_writer import write
from src.app.DB.session import get_db
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



"""TODO: make a video"""
@router.get("/")
async def read_db(model: str, request: Request):
    # 1: Mapping model.
    #    Enum "Tables" contains all tables names
    model_class = Tables.get_model(model)
    if not model_class:
        raise HTTPException(status_code=404, detail="Table not found")
    # 2: Parse the query.
    raw_filters = dict(request.query_params)
    # 3: Process filters
    processed_filters = {}
    # 4: Call function:
    results = await find_by(model_class, **processed_filters)
    return results

