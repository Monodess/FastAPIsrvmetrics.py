from enum import StrEnum, Enum

from src.app.models.models import Healthcheck, PageSpeed


class Tables(Enum):
    HEATHCHECK = Healthcheck
    PAGESPEED = PageSpeed



