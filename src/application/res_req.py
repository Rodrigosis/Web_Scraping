from typing import Dict, List
from pydantic import BaseModel, Field


class ObjRequest(BaseModel):
    # name: List[str] = Field(..., description='Manga name')
    name: str  # = Field(..., description='Manga name')


class ObjResponse(BaseModel):
    data: Dict
