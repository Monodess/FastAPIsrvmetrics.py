import pytest

from src.app.services.data_writer import *
from tests.data_mocks.mock_orm_obj import mock_orm_health_obj, mock_orm_pgspeed_obj

@pytest.mark.asyncio
async def test_write_data(mock_orm_health_obj):
    await write_data(mock_orm_health_obj)
