from pydantic import BaseModel, Field


class LocationViewPydantic(BaseModel):
    code: str = Field(max_length=128)
    name: str = Field(max_length=512)

    class Config:
        orm_mode = True
