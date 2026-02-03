import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, async_session, async_sessionmaker
from sqlalchemy import URL, create_engine, text, Result



sql = f"CREATE DATABASE IF NOT EXISTS server_metrics;"

engine = create_engine(
    url=sql,
    echo=True,
    echo_pool=True,
    # how much streams is kept alive (always)
    pool_size=5,
    max_overflow=10
)


def set_connection():
    with engine.connect() as conn:
        try:
            conn.execute(text)



