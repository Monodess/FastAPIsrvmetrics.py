#alembic + mysql alch

from sqlalchemy import Table, Column, Integer, String, DateTime, Float, Text, MetaData
from sqlalchemy.sql import func

metadata_obj = MetaData()

pagespeed_table = Table(
    "pagespeed_metrics",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("captured_at", DateTime(timezone=True), server_default=func.now(), nullable=False),
    Column("url", String(1024), nullable=False),
    Column("strategy", String(16), nullable=False),

    # Метрики из словаря return
    Column("perf_score", Float, nullable=True),  # overall_score
    Column("lcp_ms", Float, nullable=True),  # lcp
    Column("cls", Float, nullable=True),  # cls
    Column("fcp_ms", Float, nullable=True),  # fcp
    Column("speed_index_ms", Float, nullable=True),  # speed_index

    # Служебные поля
    Column("response_code", Integer, nullable=True),
    Column("error", String(512), nullable=True),
    Column("raw_json", Text, nullable=True),
)

healthcheck_table = Table(
    "healthcheck_metrics",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("captured_at", DateTime(timezone=True), server_default=func.now(), nullable=False),
    Column("url", String(1024), nullable=False),

    Column("response_code", Integer, nullable=True),  # status_code
    Column("latency_ms", Float, nullable=True),
    Column("content_length", Integer, nullable=True),  # length из return

    Column("is_up", Integer, nullable=False, server_default="0"),
    Column("error", String(512), nullable=True),
)


