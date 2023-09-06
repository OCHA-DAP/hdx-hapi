from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class LocationViewPydantic(BaseModel):
    # id: int
    code: str = Field(max_length=128)
    name: str = Field(max_length=512)
    reference_period_start: datetime
    reference_period_end: Optional[datetime]

    class Config:
        orm_mode = True
