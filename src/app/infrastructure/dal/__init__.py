"""Data Access Layer (DAL) module.

Provides abstraction for database operations including reading and writing records.
"""
from src.app.infrastructure.dal.data_reader import find_by
from src.app.infrastructure.dal.data_writer import write

__all__ = ["find_by", "write"]