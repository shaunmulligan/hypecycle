from datetime import datetime, timezone
from app.api.models import GpsReadingSchema
from app.db import gps_readings, database
from app.api import activity_crud as activity

# async def insert(reading: GpsReadingSchema):
#     # Insert a GPS reading into DB
#     ins_query = gps_readings.insert().values(latitude=reading.latitude, 
#                                             longitude=reading.longitude, 
#                                             altitude=reading.altitude, 
#                                             speed=reading.speed, 
#                                             activity_id=reading.activity_id, 
#                                             timestamp=datetime.now(timezone.utc))
#     rec = await database.execute(query=ins_query)

async def get_last_location():
    # Get the last location of an activity
    sel_query = gps_readings.select().order_by(gps_readings.c.id.desc()).limit(10)
    rec = await database.fetch_one(query=sel_query)
    return rec