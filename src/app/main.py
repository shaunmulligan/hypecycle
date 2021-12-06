from fastapi import FastAPI

from app.api import activities, ping, sensors
from app.db import database, engine, metadata

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(ping.router)
app.include_router(activities.router, prefix="/activities", tags=["activities"])
app.include_router(sensors.router, prefix="/sensors", tags=["sensors"])
