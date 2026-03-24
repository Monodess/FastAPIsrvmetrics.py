import re

import pytest
from icecream import ic
from sqlalchemy import text

from src.app.infrastructure.dal.data_reader import find_by
from src.app.infrastructure.dal.data_writer import write
from src.app.infrastructure.database.engine import db_engine
from src.app.infrastructure.database.models import Healthcheck
from src.app.schemas.contracts import Tables
from src.config.logger import Logger


@pytest.mark.asyncio
async def test_set_connection():
    try:
        v = await set_connection()
        pattern = re.compile(r"^\d+\.\d+\.\d+$")
    finally:
        await db_engine.dispose()
    assert pattern.match(v)

"""database Health check"""
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

@pytest.mark.asyncio
async def test_read_data():
    data =  await find_by(Healthcheck, id=("<", 2))
    data += await find_by(Tables.PAGESPEED.value, id=(">", 1))
    ic (data)

@pytest.mark.asyncioasync
async def test_write_data(mock_orm_health_obj):
    await write (mock_orm_health_obj)