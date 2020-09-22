#~/user-service/app/api/service.py

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from typing import Optional

from datetime import datetime, timedelta

from passlib.context import CryptContext
from jose import JWTError, jwt

from app.api.models import UserInDB, UserIn, User, TokenData
from app.api import db_manager

from devtools import debug

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "f4b284248cb60df24fe971363cd574dad7fd6d20d491e153ed9ba8b13d106875"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

async def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    debug(expires_delta)
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

async def authenticate_user(username: str, password: str):
    hashed_password = await db_manager.get_hashed_password(username)
    flag = verify_password(password, hashed_password)
    if flag == True:
        user = await db_manager.get_user(username)
    return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = await db_manager.get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user["disabled"]:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def get_password_hash(password):
    return pwd_context.hash(password)

async def create_user(payload: UserIn):
    user = UserInDB(
        username = payload.username,
        email = payload.email,
        name = payload.name,
        disabled = payload.disabled,
        hashed_password = get_password_hash(payload.password)
    )
    return await db_manager.post(user)
