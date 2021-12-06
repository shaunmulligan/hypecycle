from datetime import datetime, timezone
from app.api.models import HrReadingSchema
from app.db import hr_readings, database
from app.api import activity_crud as activity

async def insert(reading: HrReadingSchema):
    # Insert a HR reading into DB
    ins_query = hr_readings.insert().values(bpm=reading.bpm, activity_id=reading.activity_id,timestamp=datetime.now(timezone.utc))
    rec = await database.execute(query=ins_query)