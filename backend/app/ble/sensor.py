import asyncio, random
import app.api.readings_crud as readings_crud
import app.api.activity_crud as activity_crud
from app.api.models import HrReadingSchema

from bleak import BleakClient
from pycycling.heart_rate_service import HeartRateService
#globals
current_hr = 0

async def connect_to_device(address, loop, recording_interval=1):
    print("starting BLE sensor monitor loop on ", address)
    
    async with BleakClient(address, loop=loop, timeout=20.0) as client:
        
        def my_measurement_handler(data):
            global current_hr
            current_hr = data.bpm

        hr_service = HeartRateService(client)
        hr_service.set_hr_measurement_handler(my_measurement_handler)

        await hr_service.enable_hr_measurement_notifications()
        while True:
            try:
                print("Reading HRM")
                current_activity = await activity_crud.get_current()
                if current_activity is None:
                    print("No active ride. Not recording")
                    print("Current HR = ", current_hr)
                else:
                    current_activity_id = current_activity['id']
                    print("Current Activity ID: ", current_activity_id)
                    print("Current HR = ", current_hr)
                    if current_activity is not None:
                        reading = HrReadingSchema(
                            activity_id=current_activity_id,
                            bpm=current_hr
                        )
                        await readings_crud.insert(reading)

                await asyncio.sleep(recording_interval)
            except asyncio.CancelledError:
                print("cancelling ble notification")
                await hr_service.disable_hr_measurement_notifications()
                client.disconnect()
                break
