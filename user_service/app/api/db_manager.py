#~/user-service/app/api/db_manager.py

from app.api.models import UserIn, UserInDB
from app.api.db import users, database


async def post(payload: UserInDB):
    query = users.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_hashed_password(username: str):
    query = users.select(users.c.username==username)
    result = await database.fetch_one(query=query)
    return result["hashed_password"]

async def get_user(username: str):
    query = users.select().where(users.c.username==username)
    return await database.fetch_one(query=query)