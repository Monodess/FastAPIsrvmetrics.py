import datetime
from enum import Enum


from src.app.models.models import Healthcheck, PageSpeed


class Tables(Enum):
    HEALTHCHECK = Healthcheck
    PAGESPEED = PageSpeed


MAIN_FILTERS = {
    "id": int ,
    "url": str ,
    "response_code": int ,
    "captured_at": datetime,
}

HEALTH_FILTERS = {
    "latency_ms": float,
    "is_up": int
}

PAGESPEED_FILTERS = {
    "perf_score": float,
    "speed_index_ms": float,
}

