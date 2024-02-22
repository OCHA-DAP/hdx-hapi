from pydantic import ConfigDict, Field, NaiveDatetime
from typing import Optional

from hdx_hapi.endpoints.models.base import HapiBaseModel


class NationalRiskResponse(HapiBaseModel):
    risk_class: int
    global_rank: int
    overall_risk: float
    hazard_exposure_risk: float
    vulnerability_risk: float
    coping_capacity_risk: float

    meta_missing_indicators_pct: Optional[float] = None
    meta_avg_recentness_years: Optional[float] = None

    reference_period_start: Optional[NaiveDatetime]
    reference_period_end: Optional[NaiveDatetime]

    dataset_hdx_stub: str = Field(max_length=128)
    dataset_hdx_provider_stub: str = Field(max_length=128)
    resource_hdx_id: str = Field(max_length=36)

    # sector_name: str = Field(max_length=512)

    location_code: str = Field(max_length=128)
    location_name: str = Field(max_length=512)

    model_config = ConfigDict(from_attributes=True)
