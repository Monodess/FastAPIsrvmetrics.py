import pytest
from icecream import ic

from src.app.models.models import Healthcheck
from src.tests.mock_data import mock_capture_data


def mock_orm_health_obj(mock_capture_data):
    return Healthcheck(mock_capture_data[0])
h = mock_orm_health_obj()
ic(h)