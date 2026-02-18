"""
This Module contains Functions
for getting Dummy Httpx Metrics
that Data_capturer service should collect
"""
import pytest


#bassicaly we need to feed "fake data" to the func
@pytest.fixture()
def mock_capture_data():
    health_mock = {
        "url": "https://api.example.com/v1/metrics",
        "response_code": 200,
        "latency_ms": 142.5,
        "content_length": 100,
        "is_up": 1,
        "error": None
    }
    pagespeed_mock = {
        "url": "https://api.example.com/v1/metrics",
        "strategy": "mobile",
        "response_code": 200,
        "perf_score": 0.99,
        "lcp_ms": 1100.0,
        "cls": 0.01,
        "fcp_ms": 900.0,
        "speed_index_ms": 1000.0,
        "error": None
    }
    return health_mock, pagespeed_mock

