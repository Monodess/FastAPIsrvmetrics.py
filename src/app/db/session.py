from icecream import ic
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.app.db.engine import root_engine

#fabric
AsyncSessionLocal = async_sessionmaker(
    bind=root_engine,
    class_=AsyncSession,
    expire_on_commit=False
)

#generator
async def get_db():
    ic(root_engine.url)
    async with AsyncSessionLocal() as session:
        yield session
