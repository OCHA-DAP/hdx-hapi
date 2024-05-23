from pydantic import ConfigDict, Field, NaiveDatetime
from typing import Optional

from hapi_schema.utils.enums import Gender
from hdx_hapi.endpoints.middleware import mixpanel_tracking_middleware
from hdx_hapi.endpoints.models.base import HapiBaseModel, HapiModelWithAdmins


class PovertyRateResponse(HapiBaseModel):
    resource_hdx_id: str = Field(max_length=36)

    mpi: float
    headcount_ratio: float
    intensity_of_deprivation: float
    vulnerable_to_poverty: float
    in_severe_poverty: float

    reference_period_start: Optional[NaiveDatetime]
    reference_period_end: Optional[NaiveDatetime]

    location_code: str = Field(max_length=128)
    location_name: str = Field(max_length=512)
    admin1_name: Optional[str] = Field(max_length=512)

    model_config = ConfigDict(from_attributes=True)
