from app.api.models import SensorSchema
from app.db import sensors, database


async def post(payload: SensorSchema):
    query = sensors.insert().values(name=payload.name, address=payload.address)
    return await database.execute(query=query)


async def get(id: int):
    query = sensors.select().where(id == sensors.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = sensors.select()
    return await database.fetch_all(query=query)


async def put(id: int, payload: SensorSchema):
    query = (
        sensors
        .update()
        .where(id == sensors.c.id)
        .values(name=payload.name, address=payload.address)
        .returning(sensors.c.id)
    )
    return await database.execute(query=query)


async def delete(id: int):
    query = sensors.delete().where(id == sensors.c.id)
    return await database.execute(query=query)
