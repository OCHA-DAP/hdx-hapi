from datetime import datetime
from pydantic import ConfigDict, Field, NaiveDatetime
from typing import Optional

from hdx_hapi.endpoints.models.base import HapiBaseModel, HapiModelWithAdmins


class FoodSecurityResponse(HapiBaseModel, HapiModelWithAdmins):
    resource_hdx_id: str = Field(max_length=36)
    admin2_ref: int = None
    ipc_phase: str = Field(max_length=32)
    ipc_type: str = Field(max_length=32)
    population_in_phase: int
    population_fraction_in_phase: float
    reference_period_start: Optional[NaiveDatetime]
    reference_period_end: Optional[NaiveDatetime]

    model_config = ConfigDict(from_attributes=True)
