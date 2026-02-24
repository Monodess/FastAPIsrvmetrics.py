import pytest

from src.app.scheme.contracts import Tables
from src.app.services.data_reader import read_data

@pytest.mark.asyncio
async def test_read_data():
    await read_data(Tables.HEATHCHECK, id=1)
    await read_data(Tables.PAGESPEED, id=1)
