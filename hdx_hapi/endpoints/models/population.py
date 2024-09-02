import datetime
from pydantic import ConfigDict, Field
from typing import Optional

from hdx_hapi.config.doc_snippets import (
    DOC_ADMIN2_REF,
    DOC_GENDER,
    DOC_AGE_RANGE,
    DOC_HDX_RESOURCE_ID,
    DOC_REFERENCE_PERIOD_END,
    DOC_REFERENCE_PERIOD_START,
    truncate_query_description,
)
from hapi_schema.utils.enums import Gender
from hdx_hapi.endpoints.models.base import HapiBaseModel, HapiModelWithAdmins


class PopulationResponse(HapiBaseModel, HapiModelWithAdmins):
    resource_hdx_id: str = Field(max_length=36, description=truncate_query_description(DOC_HDX_RESOURCE_ID))
    admin2_ref: int = Field(description=truncate_query_description(DOC_ADMIN2_REF))

    gender: Gender = Field(description=truncate_query_description(DOC_GENDER))
    age_range: str = Field(max_length=32, description=truncate_query_description(DOC_AGE_RANGE))

    min_age: Optional[int] = Field(
        ge=0,
        description=(
            'The minimum age from `age_range`, set to `null` if `age_range` is "all" and '
            'there is no age disaggregation'
        ),
    )
    max_age: Optional[int] = Field(
        ge=0,
        description=(
            'The maximum age from `age_range`, set to `null` if `age_range` is "all" and '
            'there is no age disaggregation, or if there is no upper limit to the '
            'age range'
        ),
    )
    population: int = Field(description='The number of people')

    reference_period_start: Optional[datetime.datetime] = Field(description=DOC_REFERENCE_PERIOD_START)
    reference_period_end: Optional[datetime.datetime] = Field(description=DOC_REFERENCE_PERIOD_END)

    model_config = ConfigDict(from_attributes=True)
