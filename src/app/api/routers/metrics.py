from typing import Dict, Any

from fastapi import APIRouter, Query
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.annotation import Annotated
from starlette.requests import Request

from src.app.DAL.data_reader import find_by
from src.app.DAL.data_writer import write
from src.app.DB.session import get_db
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
def read_db(
        kwargs: Dict[str, Any],
        db: AsyncSession = Depends(get_db)
            ):
     return {"You sent", kwargs}
