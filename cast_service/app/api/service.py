#~/cast-service/app/api/service.py

from app.api.models import CastIn, CastOut, CastUpdate
from app.api import db_manager

async def create_cast(payload: CastIn):
    return await db_manager.post(payload)

async def get_cast(id: int):
    return await db_manager.get_cast(id)

async def get_all():
    return await db_manager.get_all()

async def update_cast(id: int, payload: CastUpdate):
    return await db_manager.put(id, payload)

async def delete_cast(id: int):
    return await db_manager.delete(id)