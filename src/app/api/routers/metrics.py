from fastapi import APIRouter, HTTPException
from starlette.requests import Request

from src.app.api.utils import parse_filters
from src.app.core.services.capturer import process_url
from src.app.core.services.parser import parse_both
from src.app.infrastructure.dal.data_reader import find_by
from src.app.infrastructure.dal.data_writer import write

from src.app.schemas.contracts import Tables
from src.config.app_settings import appsettings

router = APIRouter(prefix="/metrics", tags=["metrics"])

"""Captures and writes metrics for given url"""
@router.post("/")
async def capture(request: Request, url: str):
    # 1: Capturing data with web APIs
    client = request.app.state.http_client
    data = await process_url(client, url, appsettings.PAGESPEED_API_KEY)
    # 2: Parsing
    objects = parse_both(data)
    # 3: Writing to a database
    await write(objects)
    return data

"""Returns captured metrics from specified table and simple filters"""
@router.get("/")
async def read_db(model: str, request: Request):
    # 1: Mapping model.
    model_class = Tables.get_model(model)
    if not model_class:
        raise HTTPException(status_code=404, detail="Table not found")
    # 2: Parse the query.
    raw_filters = dict(request.query_params)
    # 3: Process filters
    processed_filters = parse_filters(raw_filters)
    # 4: Call function:
    results = await find_by(model_class, **processed_filters)
    return results

