from typing import List
from fastapi import APIRouter, HTTPException, Path

from app.api import activity_crud as crud
from app.api.models import ActivityDB, ActivitySchema

router = APIRouter()

@router.get("/current/", response_model=ActivityDB)
async def get_current_activity():
    activity = await crud.get_current()
    if not activity:
        raise HTTPException(status_code=404, detail="activity not found")
    return activity

@router.put("/current/stop", response_model=ActivityDB)
async def stop_current_activity():
    activity = await crud.stop_current()
    if not activity:
        raise HTTPException(status_code=404, detail="activity not found")
    return activity

@router.post("/", response_model=ActivityDB, status_code=201)
async def create_activity():
    activity = await crud.post()
    if not activity:
        raise HTTPException(status_code=404, detail="activity not found")
    return activity

@router.get("/{id}/", response_model=ActivityDB)
async def read_activity(id: int = Path(..., gt=0),):
    activity = await crud.get(id)
    if not activity:
        raise HTTPException(status_code=404, detail="activity not found")
    return activity

@router.get("/", response_model=List[ActivityDB])
async def read_all_activities():
    return await crud.get_all()

@router.put("/{id}/", response_model=ActivityDB)
async def update_activity(payload: ActivitySchema, id: int = Path(..., gt=0),):
    activity = await crud.get(id)
    if not activity:
        raise HTTPException(status_code=404, detail="activity not found")

    activity_id = await crud.put(id, payload)

    response_object = {
        "id": activity_id,
        "active": payload.active,
        "start_time": payload.start_time,
        "end_time": payload.end_time,
    }
    return response_object

@router.delete("/{id}/", response_model=ActivityDB)
async def delete_activity(id: int = Path(..., gt=0)):
    activity = await crud.get(id)
    if not activity:
        raise HTTPException(status_code=404, detail="activity not found")

    await crud.delete(id)

    return activity

