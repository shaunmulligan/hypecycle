from typing import List

from fastapi import APIRouter, HTTPException, Path

from app.api import sensor_crud as crud
from app.api.models import SensorDB, SensorSchema

router = APIRouter()

@router.post("/", response_model=SensorDB, status_code=201)
async def create_sensor(payload: SensorSchema):
    sensor_id = await crud.post(payload)

    response_object = {
        "id": sensor_id,
        "name": payload.name,
        "address": payload.address,
    }
    return response_object


@router.get("/{id}/", response_model=SensorDB)
async def read_sensor(id: int = Path(..., gt=0),):
    sensor = await crud.get(id)
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return sensor


@router.get("/", response_model=List[SensorDB])
async def read_all_sensors():
    return await crud.get_all()


@router.put("/{id}/", response_model=SensorDB)
async def update_sensor(payload: SensorSchema, id: int = Path(..., gt=0),):
    sensor = await crud.get(id)
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")

    sensor_id = await crud.put(id, payload)

    response_object = {
        "id": sensor_id,
        "name": payload.name,
        "address": payload.address,
    }
    return response_object


@router.delete("/{id}/", response_model=SensorDB)
async def delete_sensor(id: int = Path(..., gt=0)):
    sensor = await crud.get(id)
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")

    await crud.delete(id)

    return sensor


