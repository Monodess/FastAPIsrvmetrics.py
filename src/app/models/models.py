from datetime import datetime
from typing import Optional

from sqlalchemy import String, DateTime, func, Float, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.app.scheme.base import Base


class PageSpeed(Base):
    __tablename__ = "pagespeed_metrics"
    def __init__(self, _url: str, _strategy: str):
        super().__init__()
        self.url = _url
        self.strategy = _strategy

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    captured_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    url: Mapped[str] = mapped_column(String(1024))
    strategy: Mapped[str] = mapped_column(String(16))

    # Metrics (Optional[float] makes them nullable in the DB)
    perf_score: Mapped[Optional[float]] = mapped_column(Float)
    lcp_ms: Mapped[Optional[float]] = mapped_column(Float)
    cls: Mapped[Optional[float]] = mapped_column(Float)
    fcp_ms: Mapped[Optional[float]] = mapped_column(Float)
    speed_index_ms: Mapped[Optional[float]] = mapped_column(Float)

    # Service fields
    response_code: Mapped[Optional[int]] = mapped_column()
    error: Mapped[Optional[str]] = mapped_column(String(512))
    raw_json: Mapped[Optional[str]] = mapped_column(Text)


class Healthcheck(Base):
    __tablename__ = "healthcheck_metrics"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    captured_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    url: Mapped[str] = mapped_column(String(1024))

    response_code: Mapped[Optional[int]] = mapped_column()
    latency_ms: Mapped[Optional[float]] = mapped_column(Float)
    content_length: Mapped[Optional[int]] = mapped_column()

    is_up: Mapped[int] = mapped_column(server_default="0")
    error: Mapped[Optional[str]] = mapped_column(String(512))
