from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class AgeRangeViewPydantic(BaseModel):
    code: str = Field(max_length=32)
    age_min: int = None
    age_max: Optional[int] = None

    class Config:
        orm_mode = True
