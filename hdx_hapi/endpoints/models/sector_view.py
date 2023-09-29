from pydantic import BaseModel, Field


class SectorViewPydantic(BaseModel):
    code: str = Field(max_length=32)
    name: str = Field(max_length=512)

    class Config:
        orm_mode = True
