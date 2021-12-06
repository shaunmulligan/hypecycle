import os

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    MetaData,
    String,
    Table,
    Boolean,
    create_engine
)
from sqlalchemy.sql import func

from databases import Database

DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()
activities = Table(
    "activities",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("active", Boolean, default=False),
    Column("start_time", DateTime(timezone=True), default=func.now(), nullable=False),
    Column("end_time", DateTime(timezone=True), nullable=True),
)

sensors = Table(
    "sensors",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("address", String(50)),
    Column("created_date", DateTime(timezone=True), default=func.now(), nullable=False),
)

# databases query builder
database = Database(DATABASE_URL)
