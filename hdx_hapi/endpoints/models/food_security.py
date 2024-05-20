from datetime import datetime
from pydantic import ConfigDict, Field, NaiveDatetime
from typing import Optional

from hdx_hapi.endpoints.models.base import HapiBaseModel, HapiModelWithAdmins


class FoodSecurityResponse(HapiBaseModel, HapiModelWithAdmins):
    population_in_phase: int
    population_fraction_in_phase: float

    ipc_phase_code: str = Field(max_length=32)
    ipc_phase_name: str = Field(max_length=32)
    ipc_type_code: str = Field(max_length=32)

    reference_period_start: Optional[NaiveDatetime]
    reference_period_end: Optional[NaiveDatetime]

    dataset_hdx_stub: str = Field(max_length=128)
    dataset_hdx_provider_stub: str = Field(max_length=128)
    resource_hdx_id: str = Field(max_length=36)
    hapi_updated_date: datetime
    hapi_replaced_date: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)
