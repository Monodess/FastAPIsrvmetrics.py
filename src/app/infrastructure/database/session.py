from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.app.infrastructure.database.engine import db_engine
from src.config.logger import Logger

#fabric
AsyncSessionLocal = async_sessionmaker(
    bind=db_engine,
    class_=AsyncSession,
    expire_on_commit=False

)

#generator
async def get_db():
    Logger.info(db_engine.url)
    session = AsyncSessionLocal()
    try:
        yield session
    except Exception as e:
        await session.rollback()
    finally:
        await session.close()

