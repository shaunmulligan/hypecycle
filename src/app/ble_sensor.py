import asyncio, random
import app.api.readings_crud as readings_crud
import app.api.activity_crud as activity_crud
from app.api.models import HrReadingSchema

async def connect_to_device(address, loop):
    print("starting BLE sensor monitor loop on ", address)
    while True:
        try:
            print("Reading HRM")
            current_activity = await activity_crud.get_current()
            if current_activity is None:
                print("No activity active. Not recording")
            else:
                current_activity_id = current_activity['id']
                print("Current Activity ID: ", current_activity_id)
                random_reading = HrReadingSchema(bpm=random.randint(60, 200), activity_id=current_activity_id)
                await readings_crud.insert(random_reading)

            await asyncio.sleep(5)
        except asyncio.CancelledError:
            print("cancelling ble notification")
            break