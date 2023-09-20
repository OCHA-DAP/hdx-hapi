from pydantic import BaseModel, Field


class GenderViewPydantic(BaseModel):
    code: str = Field(max_length=1)
    description: str = Field(max_length=256)

    class Config:
        orm_mode = True
