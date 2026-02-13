"""
This Module contains Functions
for getting Dummy Httpx Metrics
that Data_capturer service should collect
"""
import pytest


#bassicaly we need to feed "fake data" to the func
@pytest.mark.asyncio
async def get_mock_capture_data():
    health_mock = {"url": "https://api.example.com/v1/metrics",
                   "response_code": 200,
                   "latency_ms": 142.5,
                   "content_length": 100,
                   "is_up": 1}
    pagespeed_mock = {
        "perf_score": 0.99,
        "lcp_ms": 1100,
        "cls": 0.01,
        "fcp_ms": 900,
        "speed_index_ms": 1000
    }
    return health_mock, pagespeed_mock
