from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class OrgTypeViewPydantic(BaseModel):
    code: str = Field(max_length=32)
    description: str = Field(max_length=512)

    class Config:
        orm_mode = True
