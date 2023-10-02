from pydantic import ConfigDict, Field
from typing import Optional

from hdx_hapi.endpoints.models.base import HapiBaseModel


class PopulationViewPydantic(HapiBaseModel):
    gender_code: Optional[str] = Field(max_length=1)
    age_range_code: Optional[str] = Field(max_length=32)
    population: int
    dataset_hdx_stub: str = Field(max_length=128)
    location_code: str = Field(max_length=128)
    location_name: str = Field(max_length=512)
    admin1_code: str = Field(max_length=128)
    admin1_name: str = Field(max_length=512)
    admin2_code: str = Field(max_length=128)
    admin2_name: str = Field(max_length=512)

    model_config = ConfigDict(from_attributes=True)
