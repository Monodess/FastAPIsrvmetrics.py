from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.app.DB.engine import db_engine
from src.appsetting.logger import Logger

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

