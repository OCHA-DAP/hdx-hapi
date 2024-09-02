import datetime

from hapi_schema.utils.enums import RiskClass
from pydantic import ConfigDict, Field
from typing import Optional

from hdx_hapi.config.doc_snippets import (
    DOC_HDX_RESOURCE_ID,
    DOC_LOCATION_CODE,
    DOC_LOCATION_NAME,
    DOC_REFERENCE_PERIOD_END,
    DOC_REFERENCE_PERIOD_START,
    DOC_RISK_CLASS,
    DOC_LOCATION_REF,
    truncate_query_description,
)
from hdx_hapi.endpoints.models.base import HapiBaseModel


class NationalRiskResponse(HapiBaseModel):
    risk_class: RiskClass = Field(description=truncate_query_description(DOC_RISK_CLASS))
    global_rank: int = Field(
        ge=1,
        le=250,
        description=(
            'The rank of the country based on `overall_risk`. Higher rank '
            '(smaller number) is associated with more risk.'
        ),
    )
    overall_risk: float = Field(
        ge=0,
        le=10,
        description=(
            'The INFORM composite risk index, based on a '
            'combination of 54 indicators into three dimensions of risk: hazard and '
            'exposure, vulnerability, and lack of coping capacity. Risk score '
            'is given out of 10.'
        ),
    )
    hazard_exposure_risk: float = Field(
        ge=0,
        le=10,
        description=('Risk due to events that may occur, and exposure to them. Risk score is given out of 10. '),
    )
    vulnerability_risk: float = Field(
        ge=0,
        le=10,
        description=('Risk due to hazard susceptibility. Risk score is given out of 10.'),
    )
    coping_capacity_risk: float = Field(
        ge=0,
        le=10,
        description=('Risk due to lack of coping capacity to alleviate hazard impact. Risk score is given out of 10.'),
    )

    meta_missing_indicators_pct: Optional[float] = Field(
        ge=0,
        le=100,
        description=(
            'The average of the total number of years older than the reference year '
            'per indicator, to account for any older data used as a proxy'
        ),
    )
    meta_avg_recentness_years: Optional[float] = Field(
        ge=0,
        description=(
            'The average of the total number of years older than the reference year '
            'per indicator, to account for any older data used as a proxy)'
        ),
    )

    reference_period_start: Optional[datetime.datetime] = Field(description=DOC_REFERENCE_PERIOD_START)
    reference_period_end: Optional[datetime.datetime] = Field(description=DOC_REFERENCE_PERIOD_END)

    # dataset_hdx_stub: str = Field(max_length=128)
    # dataset_hdx_provider_stub: str = Field(max_length=128)
    resource_hdx_id: str = Field(max_length=36, description=truncate_query_description(DOC_HDX_RESOURCE_ID))
    # hapi_updated_date: datetime
    # hapi_replaced_date: Optional[datetime]

    # sector_name: str = Field(max_length=512)
    location_ref: int = Field(description=truncate_query_description(DOC_LOCATION_REF))
    location_code: str = Field(max_length=128, description=truncate_query_description(DOC_LOCATION_CODE))
    location_name: str = Field(max_length=512, description=truncate_query_description(DOC_LOCATION_NAME))

    model_config = ConfigDict(from_attributes=True)
