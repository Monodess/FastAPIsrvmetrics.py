import asyncio

from icecream import ic
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from src.app.db.config import settings

root_url = settings.database_url.rsplit('/', 1)[0] + "/mysql"
db_url = settings.database_url
#in database_url mysql+aiomysql makes it async engine
root_engine = create_async_engine(
    url=root_url,
    echo=True,
    echo_pool=True,
    #how much streams is kept alive (always)
    pool_size=1,
)
db_engine = create_async_engine(
    url=db_url,
    echo=True,
    echo_pool=True,
    #how much streams is kept alive (always)
    pool_size=5,
    max_overflow=10
)
#transaction handler
AsyncSessionLocal = async_sessionmaker(
    bind=root_engine,
    class_=AsyncSession,
    expire_on_commit=False
)


