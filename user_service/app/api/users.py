#~/user-service/app/api/users.py

from fastapi import Header, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

users = APIRouter()

@users.post("/token", response_model=Token)
async def login_for_access_token(user_data: OAuth2PasswordRequestForm = Dependes()):
    user = 