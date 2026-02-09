from icecream import ic
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.app.db.engine import db_engine

#fabric
AsyncSessionLocal = async_sessionmaker(
    bind=db_engine,
    class_=AsyncSession,
    expire_on_commit=False

)

#generator
async def get_db():
    ic(db_engine.url)
    async with AsyncSessionLocal() as session:
        yield session
