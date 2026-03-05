from src.app.DB.config import Settings
from src.app.DB.session import get_db
from src.app.models.models import PageSpeed, Healthcheck
from src.appsetting.logger import Logger

settings = Settings()


async def write(data: tuple | (Healthcheck | PageSpeed)):
    try:
        async with get_db() as session:
            # add_all for iterable objects
            if isinstance(data, (list, tuple)):
                session.add_all(data)
            else:
                session.add(data)
            await session.commit()
    except Exception as e:
        await session.rollback()
        Logger.error(e)
        #raise e again so that the service will know about it
        raise e