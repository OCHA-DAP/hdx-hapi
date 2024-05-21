from pydantic import ConfigDict, Field, NaiveDatetime
from typing import Optional

from hapi_schema.utils.enums import Gender
from hdx_hapi.endpoints.models.base import HapiBaseModel, HapiModelWithAdmins


class PopulationResponse(HapiBaseModel, HapiModelWithAdmins):
    resource_hdx_id: str = Field(max_length=36)
    admin2_ref: int = None

    gender: Optional[Gender] = Field()
    age_range: Optional[str] = Field(max_length=32)

    min_age: Optional[int]
    max_age: Optional[int]
    population: int

    reference_period_start: Optional[NaiveDatetime]
    reference_period_end: Optional[NaiveDatetime]

    model_config = ConfigDict(from_attributes=True)
