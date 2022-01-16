from typing import List

from fastapi import APIRouter, HTTPException, Path

from app.api import gps_crud
from app.api.models import GpsReadingDB

router = APIRouter()

@router.get("/location/", response_model=GpsReadingDB)
async def get_location():
    """
    Get the last location from DB
    """
    location = gps_crud.get_last_location()
    if not location:
        raise HTTPException(status_code=404, detail="no location not found")
    return location