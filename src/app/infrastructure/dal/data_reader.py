"""Database read operations using SQLAlchemy ORM.

This module provides generic query functions for retrieving data from the database
with flexible filtering capabilities.
"""
from typing import Type, Optional, List, Any

from sqlalchemy import select, and_

from src.app.infrastructure.dal.contracts import OPERATORS
from src.config.database import Settings
from src.app.infrastructure.database.session import AsyncSessionLocal
from src.config.logger import Logger

settings = Settings()


async def find_by(model_class: Type, **filters) -> Optional[List[Any]]:
    """Query database records with flexible filtering.

    Supports multiple filter conditions and comparison operators. Use tuple syntax
    for comparison operators other than equality.

    Args:
        model_class: SQLAlchemy ORM model class to query.
        **filters: Keyword arguments for filtering. Values can be:
            - Simple values for equality: field=value
            - Tuples for comparisons: field=("<", 400) or field=(">", 100)

    Returns:
        List of model instances matching the filters, or None if query fails.

    Example:
        await find_by(Healthcheck, status_code=("<", 400), is_up=1)
        [Healthcheck(...), Healthcheck(...)]
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
