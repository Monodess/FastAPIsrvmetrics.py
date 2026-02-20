import re

import pytest

from src.app.services.data_writer import *

@pytest.mark.asyncio
async def test_set_connection():
    try:
        v = await set_connection()
        raw = "ashdafsafsadf"
        pattern = re.compile(r"^\d+\.\d+\.\d+$")
    finally:
        await db_engine.dispose()
    assert pattern.match(v)

@pytest.mark.asyncio
async def test_write_data(mock_orm_health_obj):
    await write_data(mock_orm_health_obj)
    assert