import pytest
from icecream import ic

from src.app.DAL.data_reader import find_by
from src.app.models.models import Healthcheck
from src.app.scheme.contracts import Tables


@pytest.mark.asyncio
async def test_read_data():
    data =  await find_by(Healthcheck, id=1)
    await find_by(Tables.PAGESPEED, id=1)
    ic (data)