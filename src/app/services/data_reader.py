"""This module implements DB reading functions
    in both Core and ORM SQL-alchemy way"""
import asyncio
import logging as log
from contextlib import asynccontextmanager

from icecream import ic

from src.app.appsetting.logger import Logger
from src.app.db.config import Settings
from src.app.db.engine import db_engine
from src.app.db.session import get_db
from src.app.scheme.contracts import Tables

settings = Settings()

"""This function uses Core Sql-alchemy 
        functions to read data"""
async def read_data(table: Tables, id: int) :
   db_context = asynccontextmanager(get_db)
   try:
        async with db_context() as session:
            data = await session.get(table.value, id)
            ic(f"Record found: {data}")
   except Exception as e:
        log.error(f"Reading went wrong: {e}")


async def main():
    try:
        await read_data(Tables.HEATHCHECK, 1) #dummy p for now
    except Exception as e:
        Logger.error("Error in main func", e)
    finally:
        await db_engine.dispose()

if __name__ == '__main__':
    asyncio.run(main())
