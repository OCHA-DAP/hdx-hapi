from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional


class PopulationViewPydantic(BaseModel):
    gender_code: Optional[str] = Field(max_length=1,required=False)
    age_range_code: Optional[str] = Field(max_length=32,required=False)
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
