from pydantic import BaseModel, Field


class NoteSchema(BaseModel):
    title: str = Field(..., min_length=3, max_length=50)
    description: str = Field(..., min_length=3, max_length=50)


class NoteDB(NoteSchema):
    id: int

class SensorSchema(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    address: str = Field(..., min_length=3, max_length=50)

class SensorDB(SensorSchema):
    id: int