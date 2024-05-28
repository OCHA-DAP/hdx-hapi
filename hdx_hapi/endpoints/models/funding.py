from pydantic import ConfigDict, Field, NaiveDatetime
from typing import Optional

from hdx_hapi.endpoints.models.base import HapiBaseModel
from hdx_hapi.endpoints.models.util.constants import NON_NEGATIVE_DECIMAL_TYPE


class FundingResponse(HapiBaseModel):
    resource_hdx_id: str = Field(max_length=36)

    appeal_code: str = Field(max_length=32)
    appeal_name: str = Field(max_length=256)
    appeal_type: str = Field(max_length=32)

    requirements_usd: NON_NEGATIVE_DECIMAL_TYPE
    funding_usd: NON_NEGATIVE_DECIMAL_TYPE
    funding_pct: NON_NEGATIVE_DECIMAL_TYPE

    location_ref: int
    location_code: str = Field(max_length=128)
    location_name: str = Field(max_length=512)

    reference_period_start: NaiveDatetime
    reference_period_end: Optional[NaiveDatetime]

    model_config = ConfigDict(from_attributes=True)
