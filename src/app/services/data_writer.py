import asyncio

from icecream import ic
from pydantic import validate_call
from sqlalchemy import text

from src.app.db.config import Settings
from src.app.db.engine import db_engine
from src.app.db.session import get_db
from src.app.models.models import PageSpeed, Healthcheck

settings = Settings()

"""DB Health check"""
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


"""Write one field"""
async def write_data(data: Healthcheck | PageSpeed):
    try:
        async for session in get_db():
            # add_all for pack-objects
            # add for single entry
            session.add(data)
            await session.commit()
            break

    except Exception as e:
     ic(e)

"""Write all fields"""
async def write_all_data(data: tuple):
    try:
        async for session in get_db():
            # add_all for pack-objects
            session.add_all(data)
            await session.commit()
            break
    except Exception as e:
     ic(e)

