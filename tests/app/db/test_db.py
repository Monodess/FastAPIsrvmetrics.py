import re

import pytest

from src.app.db.engine import db_engine
from src.app.services.data_writer import set_connection


@pytest.mark.asyncio
async def test_set_connection():
    try:
        v = await set_connection()
        pattern = re.compile(r"^\d+\.\d+\.\d+$")
    finally:
        await db_engine.dispose()
    assert pattern.match(v)
