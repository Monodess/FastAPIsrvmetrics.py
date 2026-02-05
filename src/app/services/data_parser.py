"""
Reshapes input metrics for database storage

This service receives [data] from 'data_capturer' and reshape it for DB model
with engines from 'init_engine'
"""

import asyncio

from icecream import ic
from sqlalchemy.ext.asyncio import async_session, async_sessionmaker
from sqlalchemy import URL, text, Result
from sqlalchemy.sql.coercions import expect

from src.app.db.config import settings
from src.app.db.init_engine import db_engine

from src.app.scheme.models import pagespeed_table, healthcheck_table

# from data_capturer import data



# def parse_health():
#     data[1]





