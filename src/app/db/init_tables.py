import asyncio

from src.app.db.engine import db_engine
from src.app.scheme.base import Base

async def create_tables():
    async with db_engine.begin() as conn:
       await conn.run_sync(Base.metadata.create_all)

if __name__ == '__main__':
    asyncio.run(create_tables())