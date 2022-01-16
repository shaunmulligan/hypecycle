import os

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    MetaData,
    String,
    Table,
    Boolean,
    ForeignKey,
    Float,
    create_engine
)
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base  # type: ignore
from sqlalchemy.orm import sessionmaker  # type: ignore
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

hr_readings = Table(
    'hr_readings', metadata,
    Column('id', Integer, primary_key=True),
    Column('timestamp', DateTime(timezone=True), nullable=False, index=True),
    Column('activity_id', Integer, ForeignKey("activities.id"), nullable=False),
    Column('bpm', Integer)
)

gps_readings = Table(
    'gps_readings', metadata,
    Column('id', Integer, primary_key=True),
    Column('timestamp', DateTime(timezone=True), nullable=False, index=True),
    Column('activity_id', Integer, ForeignKey("activities.id"), nullable=False),
    Column('latitude', Float),
    Column('longitude', Float),
    Column('altitude', Float),
    Column('speed', Float)
)

# databases query builder
database = Database(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()