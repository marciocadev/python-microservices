#~/cast-service/app/api/db_manager.py

from app.api.models import CastIn, CastOut, CastUpdate
from app.api.db import casts, database


async def post(payload: CastIn):
    query = casts.insert().values(**payload.dict())

    return await database.execute(query=query)


async def get_cast(id: int):
    query = casts.select(casts.c.id==id)
    return await database.fetch_one(query=query)


async def get_all():
    query = casts.select()
    return await database.fetch_all(query=query)


async def put(id: int, payload: CastUpdate):
    query = (
        casts
        .update()
        .where(id == casts.c.id)
        .values(name=payload.name, nationality=payload.nationality)
        .returning(casts.c.id)
    )
    return await database.execute(query=query)


async def delete(id: int):
    query = casts.delete().where(id == casts.c.id)
    return await database.execute(query=query)