from datetime import datetime
from pydantic import ConfigDict, Field, NaiveDatetime
from typing import Optional

from hdx_hapi.endpoints.models.base import HapiBaseModel, HapiModelWithAdmins
from hapi_schema.utils.enums import Gender, PopulationGroup, PopulationStatus, DisabledMarker


class HumanitarianNeedsResponse(HapiBaseModel, HapiModelWithAdmins):
    resource_hdx_id: str = Field(max_length=36)
    gender: Optional[Gender] = Field(max_length=32)
    age_range: Optional[str] = Field(max_length=32)
    min_age: Optional[int] = None
    max_age: Optional[int] = None
    disabled_marker: Optional[DisabledMarker] = Field(max_length=32)
    sector_code: Optional[str] = Field(max_length=32)
    population_group: Optional[PopulationGroup] = Field(max_length=32)
    population_status: Optional[PopulationStatus] = Field(max_length=32)
    population: Optional[int] = None
    reference_period_start: NaiveDatetime
    reference_period_end: Optional[NaiveDatetime]
    sector_name: Optional[str] = Field(max_length=512)

    # dataset_hdx_stub: str = Field(max_length=128)
    # dataset_hdx_provider_stub: str = Field(max_length=128)

    # hapi_updated_date: datetime
    # hapi_replaced_date: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)
