from src.config.database import Settings
from src.app.infrastructure.database.session import get_db
from src.app.infrastructure.database.models import PageSpeed, Healthcheck
from src.config.logger import Logger

settings = Settings()


async def write(data: tuple | (Healthcheck | PageSpeed)) -> None:
    """Write ORM model instances to the database.

    Handles both single objects and collections (list/tuple) of ORM instances.
    Automatically commits changes or rolls back on error.

    Args:
        data: Single ORM model instance or iterable of instances to persist.

    Raises:
        Exception: Re-raises database errors after logging and rollback.

    Example:
        health_obj = Healthcheck(url="https://example.com", is_up=1)
        await write(health_obj)
        
        health_list = [healthcheck1, healthcheck2]
        await write(health_list)
    """
    try:
        async with get_db() as session:
            if isinstance(data, (list, tuple)):
                session.add_all(data)
            else:
                session.add(data)
            await session.commit()
    except Exception as e:
        await session.rollback()
        Logger.error(e)
        raise