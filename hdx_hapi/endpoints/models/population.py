from pydantic import ConfigDict, Field, model_validator, NaiveDatetime
from typing import Optional

from hapi_schema.utils.enums import Gender
from hdx_hapi.endpoints.models.base import HapiBaseModel


class PopulationResponse(HapiBaseModel):
    resource_hdx_id: str = Field(max_length=36)
    admin2_ref: int = None

    gender: Optional[Gender] = Field()
    age_range: Optional[str] = Field(max_length=32)

    min_age: Optional[int]
    max_age: Optional[int]
    population: int

    reference_period_start: Optional[NaiveDatetime]
    reference_period_end: Optional[NaiveDatetime]

    location_ref: int = None
    location_code: str = Field(max_length=128)
    location_name: str = Field(max_length=512)

    admin1_ref: int = None
    admin1_code: Optional[str] = Field(max_length=128)
    admin1_name: Optional[str] = Field(max_length=512)
    admin1_is_unspecified: bool = Field(exclude=True)

    admin2_code: Optional[str] = Field(max_length=128)
    admin2_name: Optional[str] = Field(max_length=512)
    admin2_is_unspecified: bool = Field(exclude=True)

    model_config = ConfigDict(from_attributes=True)
