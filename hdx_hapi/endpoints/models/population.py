from pydantic import ConfigDict, Field, NaiveDatetime
from typing import Optional

from hdx_hapi.config.doc_snippets import DOC_GENDER, DOC_AGE_RANGE, truncate_query_description
from hapi_schema.utils.enums import Gender
from hdx_hapi.endpoints.models.base import HapiBaseModel, HapiModelWithAdmins


class PopulationResponse(HapiBaseModel, HapiModelWithAdmins):
    resource_hdx_id: str = Field(max_length=36)
    admin2_ref: int = None

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
    population: int

    reference_period_start: Optional[NaiveDatetime]
    reference_period_end: Optional[NaiveDatetime]

    model_config = ConfigDict(from_attributes=True)
