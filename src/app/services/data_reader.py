"""This module implements DB reading functions
    in both Core and ORM SQL-alchemy way"""
import asyncio
import logging as log
from contextlib import asynccontextmanager
from typing import Type

from icecream import ic

from src.app.appsetting.logger import Logger
from src.app.db.config import Settings
from src.app.db.engine import db_engine
from src.app.db.session import get_db
from src.app.models.models import Healthcheck
from src.app.scheme.base import Base
from src.app.scheme.contracts import Tables
from sqlalchemy import select
settings = Settings()

"""This function uses Core Sql-alchemy 
        functions to read data"""
async def find_by(model: Type[Base], **kwargs) :
    """Example: data = find_by(Healthcheck, url="https://chromewebstore.google.com/", status=200, is_up=1...)"""
    db_context = asynccontextmanager(get_db)
    try:
        async with db_context() as session:
            query = select(model).filter_by(**kwargs)
            result = await session.execute(query)
            Logger.info(f"Record found: {result}")
            return result
    except Exception as e:
        log.error(f"Reading went wrong: {e}")
        return None


async def main():
    try:
        data = await find_by(Healthcheck, "id", "1")
        ic(data)
    except Exception as e:
        Logger.error("Error in main func", e)
    finally:
        await db_engine.dispose()

if __name__ == '__main__':
    asyncio.run(unpacking(1, (3, 5 , 7), {"g": 3, "j": 4}))
    asyncio.run(main())
