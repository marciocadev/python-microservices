#~/user-service/app/api/models.py

from pydantic import BaseModel
from typing import Optional


class Token(BaseModel):
    access_token: str
    token_str: str


class TokenData(BaseModel):
    username: Optional[str] = None


class User(BaseModel):
    username: str
    email: Optional[str] = None
    name: Optional[str] = None
    disabled: Optional[bool] = None


class UserInDB(User):
    hashed_password: str