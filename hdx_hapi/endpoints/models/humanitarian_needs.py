from datetime import datetime
from pydantic import ConfigDict, Field, NaiveDatetime
from typing import Optional

from hdx_hapi.endpoints.models.base import HapiBaseModel, HapiModelWithAdmins
from hapi_schema.utils.enums import Gender, PopulationGroup, PopulationStatus, DisabledMarker


class HumanitarianNeedsResponse(HapiBaseModel, HapiModelWithAdmins):
    resource_hdx_id: str = Field(max_length=36)
    gender: Gender
    age_range: str = Field(max_length=32)
    min_age: Optional[int] = Field(ge=0)
    max_age: Optional[int] = Field(ge=0)
    disabled_marker: DisabledMarker
    sector_code: str = Field(max_length=32)
    population_group: PopulationGroup
    population_status: PopulationStatus
    population: int = Field(ge=0)
    reference_period_start: NaiveDatetime
    reference_period_end: Optional[NaiveDatetime]
    sector_name: Optional[str] = Field(max_length=512)

    model_config = ConfigDict(from_attributes=True)
