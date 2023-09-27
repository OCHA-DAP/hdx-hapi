from datetime import datetime
from pydantic import BaseModel, Field


class PopulationViewPydantic(BaseModel):
    gender_code: str = Field(max_length=1)
    age_range_code: str = Field(max_length=32)
    population: int
    dataset_hdx_stub: str = Field(max_length=128)
    location_code: str = Field(max_length=128)
    location_name: str = Field(max_length=512)
    admin1_code: str = Field(max_length=128)
    admin1_name: str = Field(max_length=512)
    admin2_code: str = Field(max_length=128)
    admin2_name: str = Field(max_length=512)

    class Config:
        orm_mode = True
