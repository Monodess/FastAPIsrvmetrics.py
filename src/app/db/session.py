from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from src.app.db.engine import db_engine

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=db_engine)

async with SessionLocal() as s:
    pass

