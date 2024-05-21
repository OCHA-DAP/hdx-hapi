from datetime import datetime
from pydantic import ConfigDict, Field, NaiveDatetime
from typing import Optional

from hdx_hapi.endpoints.models.base import HapiBaseModel, HapiModelWithAdmins


class HumanitarianNeedsResponse(HapiBaseModel, HapiModelWithAdmins):
    gender_code: Optional[str] = Field(max_length=1)
    age_range_code: Optional[str] = Field(max_length=32)
    disabled_marker: Optional[bool] = None
    sector_code: Optional[str] = Field(max_length=32)
    sector_name: Optional[str] = Field(max_length=512)
    population_status_code: Optional[str] = Field(max_length=32)
    population_group_code: Optional[str] = Field(max_length=32)
    population: int = None

    reference_period_start: Optional[NaiveDatetime]
    reference_period_end: Optional[NaiveDatetime]

    dataset_hdx_stub: str = Field(max_length=128)
    dataset_hdx_provider_stub: str = Field(max_length=128)
    resource_hdx_id: str = Field(max_length=36)

    hapi_updated_date: datetime
    hapi_replaced_date: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)
