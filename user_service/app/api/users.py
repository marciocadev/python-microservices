#~/user-service/app/api/users.py

from datetime import datetime, timedelta

from fastapi import Header, APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.api.models import UserOut, UserIn, Token, User
from app.api import service

from devtools import debug

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post('/', response_model=UserOut, status_code=201)
async def create_user(payload: UserIn):
    user_id = await service.create_user(payload)
    response = {
        'id': user_id,
        **payload.dict()
    }
    return response

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=service.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = await service.create_access_token(
        data={"sub": user["username"]},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}

@router.get("users/me", response_model=User)
async def read_users_me(current_user: User = Depends(service.get_current_active_user)):
    return current_user