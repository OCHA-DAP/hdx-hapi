from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Admin2ViewPydantic(BaseModel):
    # id: int
    # admin1_ref: int
    code: str = Field(max_length=128)
    name: str = Field(max_length=512)
    is_unspecified: bool
    reference_period_start: datetime
    reference_period_end: Optional[datetime]

    class Config:
        orm_mode = True
