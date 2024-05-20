from datetime import datetime
from pydantic import ConfigDict, Field, NaiveDatetime
from typing import Optional

from hdx_hapi.endpoints.models.base import HapiBaseModel, HapiModelWithAdmins


class PopulationResponse(HapiBaseModel, HapiModelWithAdmins):
    gender_code: Optional[str] = Field(max_length=1)
    age_range_code: Optional[str] = Field(max_length=32)
    population: int

    reference_period_start: Optional[NaiveDatetime]
    reference_period_end: Optional[NaiveDatetime]

    dataset_hdx_stub: str = Field(max_length=128)
    resource_hdx_id: str = Field(max_length=36)
    hapi_updated_date: datetime
    hapi_replaced_date: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)
