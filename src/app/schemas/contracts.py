from enum import Enum

from src.app.infrastructure.database.models import Healthcheck, PageSpeed


class Tables(Enum):
    HEALTHCHECK = Healthcheck
    PAGESPEED = PageSpeed

    @classmethod
    def get_model(cls, name: str) :
        try:
            return cls[name.upper()].value
        except KeyError:
            return None



