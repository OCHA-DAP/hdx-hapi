from hapi_schema.utils.enums import RiskClass
from pydantic import ConfigDict, Field, NaiveDatetime
from typing import Optional

from hdx_hapi.endpoints.models.base import HapiBaseModel
from hdx_hapi.endpoints.models.util.constants import PERCENTAGE_TYPE

RISK_TYPE = Field(ge=0, le=10)


class NationalRiskResponse(HapiBaseModel):
    risk_class: RiskClass
    global_rank: int = Field(ge=1, le=250)
    overall_risk: float = RISK_TYPE
    hazard_exposure_risk: float = RISK_TYPE
    vulnerability_risk: float = RISK_TYPE
    coping_capacity_risk: float = RISK_TYPE

    meta_missing_indicators_pct: Optional[float] = PERCENTAGE_TYPE
    meta_avg_recentness_years: Optional[float] = Field(ge=0)

    reference_period_start: Optional[NaiveDatetime]
    reference_period_end: Optional[NaiveDatetime]

    # dataset_hdx_stub: str = Field(max_length=128)
    # dataset_hdx_provider_stub: str = Field(max_length=128)
    resource_hdx_id: str = Field(max_length=36)
    # hapi_updated_date: datetime
    # hapi_replaced_date: Optional[datetime]

    # sector_name: str = Field(max_length=512)

    location_code: str = Field(max_length=128)
    location_name: str = Field(max_length=512)

    model_config = ConfigDict(from_attributes=True)
