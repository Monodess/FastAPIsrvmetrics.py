import re

import pytest
from icecream import ic
from sqlalchemy import text

from src.app.appsetting.logger import Logger
from src.app.db.engine import db_engine



@pytest.mark.asyncio
async def test_set_connection():
    try:
        v = await set_connection()
        pattern = re.compile(r"^\d+\.\d+\.\d+$")
    finally:
        await db_engine.dispose()
    assert pattern.match(v)

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
            Logger.error(f"Connection failed: {e}")
            return None