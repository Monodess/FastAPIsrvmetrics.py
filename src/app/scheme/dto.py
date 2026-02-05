from sqlalchemy import Table, Column, Integer, String, DateTime, Float, Text, MetaData
from sqlalchemy.sql import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class PageSpeed(Base):
    pass