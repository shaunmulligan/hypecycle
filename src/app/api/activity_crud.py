from app.api.models import ActivitySchema
from app.db import activities, database
from datetime import datetime, timezone

async def post():
    #first set all other activities to inactive
    up_query = "UPDATE activities SET active = false WHERE active IS true"
    await database.execute(query=up_query)
    # When we create an activity, we set the time to now and active true.
    ins_query = activities.insert().values(active=True, start_time=datetime.now(timezone.utc))
    rec = await database.execute(query=ins_query)
    # Return the id of the new record and we send back the record to the client.
    query = activities.select().where(rec == activities.c.id)
    return await database.fetch_one(query=query)

async def stop_activity():
    pass

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
