"""This module implements DB reading functions
    in both Core and ORM SQL-alchemy way"""
import asyncio

from icecream import ic

from src.app.db.config import Settings
from src.app.db.session import get_db
from src.app.scheme.contracts import Tables

settings = Settings()

"""This function uses Core Sql-alchemy 
        functions to read data"""
async def read_data(table: str, id: int) :
    try:
        async for session in get_db():
            data = await session.get(table, id)
            ic(data)
            break
    except ExceptionGroup as e:
        ic(f"Reading went wrong: {e}")

if __name__ == '__main__':
     asyncio.run(read_data(Tables.HEATHCHECK, 1))
