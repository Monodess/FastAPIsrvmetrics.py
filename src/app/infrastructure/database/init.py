"""Database initialization and setup"""
from sqlalchemy import text
from src.app.infrastructure.database.engine import root_engine, db_engine
from src.app.schemas.base import Base
from src.config.logger import Logger



async def setup_database():
   """Create database if it doesnt exist"""
   async with root_engine.begin() as conn:
        try:
            await conn.execute(text("CREATE DATABASE server_metrics"))
            Logger.info("Database created successfully")
        except Exception as e:
            Logger.info("Database already exists or connection failed")
   await root_engine.dispose()

async def create_tables():
    """Create all ORM tables"""
    async with db_engine.begin() as conn:
        try:
            await conn.run_sync(Base.metadata.create_all)
            Logger.info("Tables created successfully")
        except Exception as e:
            Logger.error(f"Failed to create tables: {e}")
    await db_engine.dispose()

async def initialize_db():
    await setup_database()
    await create_tables()

import asyncio
if __name__ == '__main__':
   asyncio.run (initialize_db())
