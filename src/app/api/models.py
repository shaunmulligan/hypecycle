from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ActivitySchema(BaseModel):
    active: bool
    start_time: datetime
    end_time: Optional[datetime] = Field(...)

class ActivityDB(ActivitySchema):
    id: int

class SensorSchema(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    address: str = Field(..., min_length=3, max_length=50)

class SensorDB(SensorSchema):
    id: int

class HrReadingSchema(BaseModel):
    bpm: int
    activity_id: int

class HrReadingDB(HrReadingSchema):
    id: int
    timestamp: datetime