from fastapi import FastAPI
import asyncio
from app.api import activities, ping, sensors
from app.db import database, engine, metadata
from . import ble_sensor as ble

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    print("Startup")
    await database.connect()
    addresses = ["D9:38:0B:2E:22:DD"] # Addresses of the BLE devices to connect to.
    loop = asyncio.get_event_loop() # should return the loop fastapi is already using
    # # Launch asyncio executor for GPS monitoring
    # gps_mon_loop = loop.run_in_executor(None, location.monitor_gps, gps_stop_event)
    # Launch asyncio tasks for each ble device
    for address in addresses:
        asyncio.create_task(ble.connect_to_device(address, loop))


@app.on_event("shutdown")
async def shutdown():
    print("Shutting down")
    await database.disconnect()
    # gps_stop_event.set() # send event to stop GPS loop
    # for task in asyncio.all_tasks():
    #     task.cancel() # cancel all tasks


app.include_router(ping.router)
app.include_router(activities.router, prefix="/activities", tags=["activities"])
app.include_router(sensors.router, prefix="/sensors", tags=["sensors"])
