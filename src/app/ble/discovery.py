"""
BLE device discovery module
"""

import asyncio
from bleak import discover
from ble_service_uuids import service_uuids

async def main():
    devices = await discover_devices()
    for d in devices:
        print(d)

async def discover_devices():
    """Discover all nearby relevant BLE devices and return them as a list"""
    raw_devices = await discover()
    devices = []
    for d in raw_devices:
        info = await get_device_info(d)
        if info:
            devices.append(info)
    return devices

async def get_device_info(device):
    if device.metadata['uuids']:
        for uuid in device.metadata['uuids']:
            uuid = uuid.split('-')[0].lstrip('0').upper()
            type = next((item for item in service_uuids if item["uuid"] == uuid), None) # Check to see if we know the type of device
            if type: # If we do, add it to the list
                return {"name": device.name, "address": device.address, "type": type["name"], "identifier": type["identifier"]}

if __name__ == "__main__":
    import os

    os.environ["PYTHONASYNCIODEBUG"] = str(1)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


# {'address': 'F0:99:19:59:B4:00',
#  'details': {'path': '/org/bluez/hci0/dev_F0_99_19_59_B4_00',
#              'props': {'Adapter': '/org/bluez/hci0',
#                        'Address': 'F0:99:19:59:B4:00',
#                        'AddressType': 'public',
#                        'Alias': 'Forerunner 945',
#                        'Blocked': False,
#                        'Connected': False,
#                        'LegacyPairing': False,
#                        'Name': 'Forerunner 945',
#                        'Paired': False,
#                        'RSSI': -85,
#                        'ServicesResolved': False,
#                        'Trusted': False,
#                        'UUIDs': ['0000180d-0000-1000-8000-00805f9b34fb']}},
#  'metadata': {'manufacturer_data': {},
#               'uuids': ['0000180d-0000-1000-8000-00805f9b34fb']},
#  'name': 'Forerunner 945',
#  'rssi': -85}