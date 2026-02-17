from datetime import datetime
from typing import Optional

from sqlalchemy import String, DateTime, func, Float, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.app.scheme.alchemy_tables import healthcheck_table, pagespeed_table
from src.app.scheme.base import Base

"""
Fields for both Health and PgSpeed
"""
class AuditMixin:
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    captured_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    url: Mapped[str] = mapped_column(String(1024))
    response_code: Mapped[Optional[int]] = mapped_column()

    error: Mapped[Optional[str]] = mapped_column(String(512))
    raw_json: Mapped[Optional[str]] = mapped_column(Text)

"""
Object for both Health and PgSpeed created in [data_parser] 
"""
class Healthcheck(Base, AuditMixin):
    __tablename__ = "healthcheck_metrics"
    # __table__ = healthcheck_table

    latency_ms: Mapped[Optional[float]] = mapped_column(Float)
    content_length: Mapped[Optional[int]] = mapped_column()
    is_up: Mapped[int] = mapped_column(server_default="0")

class PageSpeed(Base, AuditMixin):
    __tablename__ = "pagespeed_metrics"
    # __table__ = pagespeed_table
    def __repr__(self) :
        vars(self)

    strategy: Mapped[str] = mapped_column(String(16))

    perf_score: Mapped[Optional[float]] = mapped_column(Float)
    lcp_ms: Mapped[Optional[float]] = mapped_column(Float)
    cls: Mapped[Optional[float]] = mapped_column(Float)
    fcp_ms: Mapped[Optional[float]] = mapped_column(Float)
    speed_index_ms: Mapped[Optional[float]] = mapped_column(Float)



