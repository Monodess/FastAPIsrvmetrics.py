"""This module implements DB reading functions
    in both Core and ORM SQL-alchemy way"""
import logging as log
from contextlib import asynccontextmanager
from typing import Type, Optional, List, Any

from fastapi.params import Query
from sqlalchemy import select, and_

from src.app.DAL.contracts import OPERATORS
from src.app.DB.config import Settings
from src.app.DB.session import get_db, AsyncSessionLocal
from src.app.models.models import Healthcheck
from src.app.scheme.contracts import Tables
from src.appsetting.logger import Logger

settings = Settings()

"""This function uses Core Sql-alchemy 
        functions to read data"""

async def find_by(model_class: Type, **filters ) -> Optional[List[Any]]:
    """
    Generic finder using SQLAlchemy
        Usage:
            await find_by(Healthcheck, status_code=("<", 400), is_up=1)

    """
    async with AsyncSessionLocal() as session:
        try:
            query = select(model_class)
            conditions = []

            for field_name, value in filters.items():
                attr = getattr(model_class, field_name, None)
                if attr is None:
                    continue
                if isinstance(value, tuple) and len(value) == 2:
                    op_str, val = value
                    if op_str in OPERATORS:
                        conditions.append(OPERATORS[op_str](attr, val))
                    else:
                        conditions.append(attr == value)
                else:
                    conditions.append(attr == value)
            if conditions:
                query = query.where(and_(*conditions))

            result = await session.execute(query)
            records = result.scalars().all()

            Logger.info(f"Found {len(records)} records for {model_class}")
            return records
        except Exception as e:
            Logger.error(f"Database query failed: {e}")
            return None
