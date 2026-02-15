import pytest
from icecream import ic
from src.app.services.data_parser import parse_health, parse_pagespeed
from src.tests.mock_data import mock_capture_data

@pytest.mark
def test_parsing(mock_capture_data):
    data = mock_capture_data
    ic(parse_health(data[1]))