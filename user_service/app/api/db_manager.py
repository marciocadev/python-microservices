#~/user-service/app/api/db_manager.py

from app.api.model import UserIn
from api.api.db import users, database


async def post(payload: UserIn):
    query users.insert().values(**payload.dict())
    return await database.execute(query=query)