from pydantic import ConfigDict, Field, NaiveDatetime
from typing import Optional

from hdx_hapi.config.doc_snippets import (
    DOC_ADMIN1_NAME,
    DOC_HDX_RESOURCE_ID,
    DOC_LOCATION_CODE,
    DOC_LOCATION_NAME,
    DOC_REFERENCE_PERIOD_END,
    DOC_REFERENCE_PERIOD_START,
    truncate_query_description,
)
from hdx_hapi.endpoints.models.base import HapiBaseModel


class PovertyRateResponse(HapiBaseModel):
    resource_hdx_id: str = Field(max_length=36, description=truncate_query_description(DOC_HDX_RESOURCE_ID))

    mpi: float = Field(
        description=(
            'The multidimensional poverty index, derived as a product of the '
            '`headcount_ratio` and `intensity_of_deprivation`. Note that this '
            'metric is presented as a fraction, while the others are percentages.'
        )
    )
    headcount_ratio: float = Field(description='The percentage of people deprived in 33% or more indicators')
    intensity_of_deprivation: float = Field(
        description='The average proportion of indicators in which people are deprived, given as a percentage.'
    )
    vulnerable_to_poverty: float = Field(description='The percentage of people deprived in 20-33% of indicators')
    in_severe_poverty: float = Field(description='The percentage of people deprived in 50% or more indicators')

    reference_period_start: Optional[NaiveDatetime] = Field(description=DOC_REFERENCE_PERIOD_START)
    reference_period_end: Optional[NaiveDatetime] = Field(description=DOC_REFERENCE_PERIOD_END)

    location_code: str = Field(max_length=128, description=truncate_query_description(DOC_LOCATION_CODE))
    location_name: str = Field(max_length=512, description=truncate_query_description(DOC_LOCATION_NAME))
    admin1_name: Optional[str] = Field(max_length=512, description=truncate_query_description(DOC_ADMIN1_NAME))

    model_config = ConfigDict(from_attributes=True)
