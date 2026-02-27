from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.appsetting.logger import Logger
from src.app.db.engine import db_engine

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

