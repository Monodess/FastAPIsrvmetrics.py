import asyncio

from icecream import ic
from sqlalchemy.ext.asyncio import async_session, async_sessionmaker
from sqlalchemy import URL, text, Result
from sqlalchemy.sql.coercions import expect

from src.app.db.config import settings
from src.app.db.engine import db_engine
from src.app.db.session import get_db
from src.app.models.models import PageSpeed

"""Health check"""


async def set_connection():
    # Ensure db_engine is an AsyncEngine
    async with db_engine.connect() as conn:
        try:
            result = await conn.execute(text("SELECT VERSION()"))
            version_str = result.scalar()
            # 3. Await the commit
            await conn.commit()
            return version_str

        except Exception as e:
            ic(f"Connection failed: {e}")


async def call_set_connection():
    try:
        return await set_connection()
    finally:
        await db_engine.dispose()


async def write_data():
    try:
        async for session in get_db():
            # add_all for pack-objects
            # add for
            session.add(data_p)
            await session.commit()
            break

    except Exception as e:
     ic(e)

data_p = PageSpeed("some url", "some strategy")

#from data_capturer import data
if __name__ == '__main__':
    res = asyncio.run(call_set_connection())
    ic(res)
    asyncio.run(write_data())
