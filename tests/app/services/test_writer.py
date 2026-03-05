import pytest

from tests.data_mocks.mock_orm_obj import mock_orm_health_obj, mock_orm_both_obj


@pytest.mark.asyncio
async def test_write_data(mock_orm_health_obj):
    await write_data(mock_orm_health_obj)

@pytest.mark.asyncio
async def test_write_all_data(mock_orm_both_obj):
    await write_all_data(mock_orm_both_obj)

