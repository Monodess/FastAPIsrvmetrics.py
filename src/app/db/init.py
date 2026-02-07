from icecream import ic
#engine dispose kills all pool
#engine begin opens pool (5)
#engine is still alive after dispose. not connected
from sqlalchemy import text

from src.app.db.engine import AsyncSessionLocal, root_engine, db_engine
from src.app.db.alchemy_tables import metadata_obj

#generator
async def get_db():
    ic(root_engine.url)
    async with AsyncSessionLocal() as session:
        yield session

#db health check
async def setup_database():
   async with root_engine.begin() as conn:
        try:
            await conn.execute(text("CREATE DATABASE server_metrics"))
            print("database was created")
        except Exception as e:
            print("database already exists or connection failed")
   await root_engine.dispose()

#create tables with sqlalchemy Tables from "alchemy_tables.py" (not ORM way)
async def create_tables():
    ic(db_engine.url)
    async with db_engine.begin() as conn:
        try:
            await conn.run_sync(metadata_obj.drop_all())
            #await conn.run_sync(metadata_obj.create_all)
        except Exception as e:
            print("failed ")
    await db_engine.dispose()



import asyncio
if __name__ == '__main__':
   asyncio.run (setup_database())
   asyncio.run (create_tables())
