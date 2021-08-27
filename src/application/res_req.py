from typing import Dict
from pydantic import BaseModel, Field


class ObjRequest(BaseModel):
    name: str = Field(..., description='Manga name')


class ObjResponse(BaseModel):
    data: Dict
