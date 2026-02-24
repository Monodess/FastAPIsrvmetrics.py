from src.app.services.data_parser import parse_health, parse_pagespeed
from tests.data_mocks.mock_data import mock_capture_data


def test_parsing(mock_capture_data):
    health_data = parse_health(mock_capture_data[0])
    pagespeed_data = parse_pagespeed(mock_capture_data[1])

    assert health_data.url == mock_capture_data[0]["url"]
    assert pagespeed_data.url == mock_capture_data[1]["url"]