#~/python-microservices/cast-service/app/api/models.py

from pydantic import BaseModel
from typing import List, Optional


class CastIn(BaseModel):
    name: str
    nationality: Optional[str] = None


class CastOut(CastIn):
    id: int

    class Config:
        schema_extra = {
            "example": {
                "id": "Unique identifier",
                "name": "Cast Name",
                "nationality": "Cast nationality"
            }
        }


class CastUpdate(CastIn):
    name: Optional[str] = None