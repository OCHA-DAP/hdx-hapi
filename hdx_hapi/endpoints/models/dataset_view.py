from pydantic import BaseModel, Field
from typing import Optional


class DatasetViewPydantic(BaseModel):
    # id: int
    code: str = Field(max_length=128)
    title: str = Field(max_length=1024)
    provider_code: str = Field(max_length=128)
    provider_name: str  = Field(max_length=512)
    hdx_link: str = Field(max_length=512)
    api_link: str = Field(max_length=1024)

    class Config:
        orm_mode = True
