#~/python-microservices/cast-service/app/api/casts.py

from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import CastOut, CastIn, CastUpdate
from app.api import service

from devtools import debug

router = APIRouter()


@router.post('/', response_model=CastOut, status_code=201)
async def create_cast(payload: CastIn):
    cast_id = await service.create_cast(payload)

    response = {
        'id': cast_id,
        **payload.dict()
    }

    debug(response)
    return response


@router.get('/{id}/', response_model=CastOut)
async def get_cast(id: int):
    cast = await service.get_cast(id)
    if not cast:
        raise HTTPException(status_code=404, detail="Cast not found")
    return cast


@router.get("/", response_model=List[CastOut])
async def get_all():
    return await service.get_all()


@router.put("/{id}/", response_model=CastOut)
async def update_cast(payload: CastUpdate, id: int):
    cast = await service.get_cast(id)
    if not cast:
        raise HTTPException(status_code=404, detail="Cast not found")

    cast_id = await service.update_cast(id, payload)

    response_object = {
        "id": cast_id,
        "name": payload.name,
        "nationality": payload.nationality,
    }
    return response_object


@router.delete("/{id}", response_model=CastOut)
async def delete_cast(id: int):
    cast = await service.get_cast(id)
    if not cast:
        raise HTTPException(status_code=404, detail="Cast not found")

    await service.delete_cast(id)
    return cast
