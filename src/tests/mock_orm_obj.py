import pytest
from icecream import ic

from src.app.models.models import Healthcheck, PageSpeed
from src.tests.mock_data import mock_capture_data

@pytest.fixture()
def mock_orm_health_obj(mock_capture_data):
    return Healthcheck(**mock_capture_data[0])

@pytest.fixture()
def mock_orm_pgspeed_obj(mock_capture_data):
    return PageSpeed(**mock_capture_data[1])

@pytest.fixture()
def mock_orm_both_obj(mock_capture_data):
    return Healthcheck(**mock_capture_data[0]), PageSpeed(**mock_capture_data[1])