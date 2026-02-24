import pytest
from icecream import ic

from tests.data_mocks.mock_data import mock_capture_data
from src.app.models.models import Healthcheck, PageSpeed

@pytest.fixture()
def mock_orm_health_obj(mock_capture_data):
    return Healthcheck(**mock_capture_data[0])
data = mock_orm_health_obj

@pytest.fixture()
def mock_orm_pgspeed_obj(mock_capture_data):
    return PageSpeed(**mock_capture_data[1])

@pytest.fixture()
def mock_orm_both_obj(mock_capture_data):
    return Healthcheck(**mock_capture_data[0]), PageSpeed(**mock_capture_data[1])

