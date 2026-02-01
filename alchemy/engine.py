from sqlalchemy.ext.asyncio import create_async_engine, async_session, async_sessionmaker
from sqlalchemy import URL, create_engine, text

from config import settings

sql= f"CREATE DATABASE IF NOT EXISTS server_metrics;"
engine = create_async_engine(
    url=settings.database_url,
    echo=True,
    echo_pool=True,
    #how much streams is kept alive (always)
    pool_size=5,
    max_overflow=10
)

async def async_conn():
    async with engine.begin() as conn:
        conn.execute(text(sql))

