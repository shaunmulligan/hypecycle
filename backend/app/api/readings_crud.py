from datetime import datetime, timezone
from app.api.models import HrReadingSchema
from app.db import hr_readings, database
from app.api import activity_crud as activity

async def insert(reading: HrReadingSchema):
    # Insert a HR reading into DB
    ins_query = hr_readings.insert().values(bpm=reading.bpm, activity_id=reading.activity_id,timestamp=datetime.now(timezone.utc))
    rec = await database.execute(query=ins_query)

async def get_last_hr():
    # Get the last HR reading
    sel_query = hr_readings.select().order_by(hr_readings.c.id.desc()).limit(10)
    rec = await database.fetch_one(query=sel_query)
    return rec