#~/user-service/app/api/users.py

from fastapi import Header, APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}

# @router.get("users/me")
# async def read_users_me(current_user: User = Depends(get_current_user)):
#     return current_user