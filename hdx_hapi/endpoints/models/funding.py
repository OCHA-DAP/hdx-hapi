from pydantic import ConfigDict, Field, NaiveDatetime
from typing import Optional

from hdx_hapi.config.doc_snippets import (
    DOC_HDX_RESOURCE_ID,
    DOC_LOCATION_CODE,
    DOC_LOCATION_HAS_HRP,
    DOC_LOCATION_IN_GHO,
    DOC_LOCATION_NAME,
    DOC_LOCATION_REF,
    DOC_REFERENCE_PERIOD_END,
    DOC_REFERENCE_PERIOD_START,
    truncate_query_description,
)
from hdx_hapi.endpoints.models.base import HapiBaseModel
from hdx_hapi.endpoints.models.util.constants import NON_NEGATIVE_DECIMAL_TYPE


class FundingResponse(HapiBaseModel):
    resource_hdx_id: str = Field(max_length=36, description=DOC_HDX_RESOURCE_ID)

    appeal_code: str = Field(max_length=32, description='A unique code given by FTS to each appeal')
    appeal_name: str = Field(max_length=256, description='Name of the appeal')
    appeal_type: str = Field(max_length=32, description='The type of the appeal, such as flash or HRP')

    requirements_usd: NON_NEGATIVE_DECIMAL_TYPE = Field(description='The funding requirements in US dollars')
    funding_usd: NON_NEGATIVE_DECIMAL_TYPE = Field(description='The actual funding in US dollars')
    funding_pct: NON_NEGATIVE_DECIMAL_TYPE = Field(
        description='The percentage of required funding received by the appeal'
    )

    location_ref: int = Field(description=truncate_query_description(DOC_LOCATION_REF))
    location_code: str = Field(max_length=128, description=truncate_query_description(DOC_LOCATION_CODE))
    location_name: str = Field(max_length=512, description=truncate_query_description(DOC_LOCATION_NAME))

    reference_period_start: NaiveDatetime = Field(description=DOC_REFERENCE_PERIOD_START)
    reference_period_end: Optional[NaiveDatetime] = Field(description=DOC_REFERENCE_PERIOD_END)

    model_config = ConfigDict(from_attributes=True)
