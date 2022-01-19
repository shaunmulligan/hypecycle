from fastapi import APIRouter
from fastapi import WebSocket, WebSocketDisconnect
import asyncio
from datetime import datetime, timezone

from app.api import gps_crud
from app.api import readings_crud
from app.api import activity_crud

router = APIRouter()

class ConnectionManager:
    """websocket connection manager"""
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    def list(self):
        """List the active ws connections"""
        return self.active_connections

manager = ConnectionManager()

@router.get("/ping")
async def pong():
    # some async operation could happen here
    # example: `notes = await get_all_notes()`
    return {"ping": "pong!"}

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            activity = await activity_crud.get_current()
            location = await gps_crud.get_last_location()
            hr = await readings_crud.get_last_hr()

            await websocket.send_json(
                {"heartrate": hr["bpm"],
                 "speed": round(location["speed"], 2),
                 "power": 201,
                 "elapsedTime": int((datetime.now(timezone.utc) - activity["start_time"]).total_seconds()) if activity else 0,
                 "avgSpeed": 20.3,
                 "cadence": 80,
                 "latitude": location["latitude"],
                 "longitude": location["longitude"],
                 "altitude": location["altitude"],
                })
            await asyncio.sleep(1)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
    except asyncio.exceptions.CancelledError:
        manager.disconnect(websocket)