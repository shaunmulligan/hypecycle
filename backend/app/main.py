from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import asyncio, os, threading
from app.api import activities, ping, sensors
from app.api import data_routes as data
from app.db import database, engine, metadata
from app.ble import sensor as ble
from app.location import gps

metadata.create_all(engine)

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
gps_stop_event = threading.Event()
os.environ["PYTHONASYNCIODEBUG"] = str(1)
location = gps.Location()

@app.on_event("startup")
async def startup():
    print("Startup")
    await database.connect()
    addresses = ["F0:99:19:59:B4:00"] # Addresses of the BLE devices to connect to.
    loop = asyncio.get_event_loop() # should return the loop fastapi is already using
    # # Launch asyncio executor for GPS monitoring
    gps_mon_loop = loop.run_in_executor(None, location.monitor_gps, gps_stop_event)
    # Launch asyncio tasks for each ble device
    for address in addresses:
        asyncio.create_task(ble.connect_to_device(address, loop, recording_interval=5))


@app.on_event("shutdown")
async def shutdown():
    print("Shutting down")
    await database.disconnect()
    gps_stop_event.set() # send event to stop GPS loop
    for task in asyncio.all_tasks():
        task.cancel() # cancel all tasks

app.include_router(ping.router)
app.include_router(activities.router, prefix="/activities", tags=["activities"])
app.include_router(sensors.router, prefix="/sensors", tags=["sensors"])
app.include_router(data.router, prefix="/data", tags=["data"])
