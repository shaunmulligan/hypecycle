from app.api.models import ActivitySchema
from app.db import activities, database


async def post(payload: ActivitySchema):
    query = activities.insert().values(active=payload.active, start_time=payload.start_time, end_time=payload.end_time)
    return await database.execute(query=query)


async def get(id: int):
    query = activities.select().where(id == activities.c.id)
    return await database.fetch_one(query=query)

async def get_current():
    query = activities.select().where(activities.c.active == True)
    rec = await database.fetch_one(query=query)
    print(dict(rec.items()))
    return rec

async def get_all():
    query = activities.select()
    return await database.fetch_all(query=query)


async def put(id: int, payload: ActivitySchema):
    query = (
        activities
        .update()
        .where(id == activities.c.id)
        .values(active=payload.active, start_time=payload.start_time, end_time=payload.end_time)
        .returning(activities.c.id)
    )
    return await database.execute(query=query)


async def delete(id: int):
    query = activities.delete().where(id == activities.c.id)
    return await database.execute(query=query)
