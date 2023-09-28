from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Admin2ViewPydantic(BaseModel):
    code: str = Field(max_length=128)
    name: str = Field(max_length=512)

    admin1_code: str = Field(max_length=128)
    admin1_name: str = Field(max_length=512)

    location_code: str = Field(max_length=128)
    location_name: str = Field(max_length=512)
    class Config:
        orm_mode = True
