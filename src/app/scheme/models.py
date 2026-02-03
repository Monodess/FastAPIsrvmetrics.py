#alembic + mysql alch

from sqlalchemy import Table, Column, Integer, String, DateTime, Float, Text, MetaData
from sqlalchemy.sql import func

metadata_obj = MetaData()

pagespeed_table = Table(
    "pagespeed_metrics",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),

    # when we captured it
    Column("captured_at", DateTime(timezone=True), server_default=func.now(), nullable=False),

    # what we measured
    Column("url", String(1024), nullable=False),
    Column("strategy", String(16), nullable=False),  # "mobile" / "desktop"

    # request/transport info
    Column("response_code", Integer, nullable=True),
    Column("latency_ms", Float, nullable=True),
    Column("error", String(512), nullable=True),

    # key lighthouse metrics (nullable because json can change / missing)
    Column("perf_score", Float, nullable=True),  # 0..1 typically
    Column("lcp_ms", Float, nullable=True),
    Column("inp_ms", Float, nullable=True),
    Column("cls", Float, nullable=True),
    Column("fcp_ms", Float, nullable=True),
    Column("ttfb_ms", Float, nullable=True),
    Column("speed_index_ms", Float, nullable=True),

    # store full response for future parsing/debugging
    Column("raw_json", Text, nullable=False),
)

healthcheck_table = Table(
    "healthcheck_metrics",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),

    Column("captured_at", DateTime(timezone=True), server_default=func.now(), nullable=False),
    Column("url", String(1024), nullable=False),

    Column("response_code", Integer, nullable=True),
    Column("latency_ms", Float, nullable=True),

    # "is_up" is basically: success + status in 200..399 (you decide in code)
    Column("is_up", Integer, nullable=False, server_default="0"),  # 0/1 for SQLite compatibility
    Column("error", String(512), nullable=True),
)



