import asyncio
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.background import BackgroundTasks
from fastapi.params import Depends
from sqlalchemy.orm import Session

from src.app.api.dto import Url
from src.app.db.init import get_db
from src.app.core.appsettings import appsettings
from src.app.services.data_capturer import loop, URLS
from loguru import logger
app = FastAPI()

"""Worker func
A worker function is an async function that performs background tasks.
It usually runs without direct user awareness and processes jobs
such as IO, computations, or message handling.
The result is typically stored or passed to another system
(database, queue, cache) rather than returned to the caller.
"""
#Background worker (after returning result starts capturing data and writes it ro db)
async def run_data_capturer(url: Url):
    try:
        data = await loop(url, appsettings.PAGESPEED_API_KEY)
        await write(data)
    except Exception as e:
        #TODO: put logging here (Loguru lib)
        logger.info("Error in bg task")


@app.post("/metrics")
async def metrics(url: Url, background_task: BackgroundTasks):
    background_task.add_task(run_data_capturer, url)
    return {"status": "accepted"}
