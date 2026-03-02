"""This module implements DB reading functions
    in both Core and ORM SQL-alchemy way"""
import logging as log
from contextlib import asynccontextmanager
from typing import Type

from fastapi.params import Query
from sqlalchemy import select

from src.app.DB.config import Settings
from src.app.DB.session import get_db
from src.app.scheme.base import Base
from src.app.scheme.contracts import Tables
from src.appsetting.logger import Logger

settings = Settings()

"""This function uses Core Sql-alchemy 
        functions to read data"""


async def common_query_params() :
    q: str | None = Query(None, description="Search Term"),
    limit: int = Query(100, ge=1, le=100),
    offset: int = Query(0, ge=0),
    sort: str = Query ("id", regex="^(id|name|date)$")
async def find_by(table: str, **kwargs) :
    """Example: data = await find_by(Healthcheck, url="https://chromewebstore.google.com/", status=200, is_up=1...)"""
    db_context = asynccontextmanager(get_db)
    try:
        async with db_context() as session:
            model = Tables(table)
            query = select(model).filter_by(**kwargs)
            result = await session.execute(query)
            Logger.info(f"Record found: {result}")
            return result.scalars().all()
    except Exception as e:
        log.error(f"Reading went wrong: {e}")
        return None

