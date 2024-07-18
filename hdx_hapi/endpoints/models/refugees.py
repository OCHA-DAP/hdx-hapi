from pydantic import ConfigDict, Field, NaiveDatetime
from typing import Optional

from hdx_hapi.config.doc_snippets import (
    DOC_GENDER,
    DOC_HDX_RESOURCE_ID,
    DOC_POPULATION_GROUP,
    DOC_AGE_RANGE,
    DOC_REFERENCE_PERIOD_END,
    DOC_REFERENCE_PERIOD_START,
    truncate_query_description,
)
from hdx_hapi.endpoints.models.base import HapiBaseModel
from hapi_schema.utils.enums import Gender, PopulationGroup


class RefugeesResponse(HapiBaseModel):
    resource_hdx_id: str = Field(max_length=36, description=truncate_query_description(DOC_HDX_RESOURCE_ID))
    origin_location_ref: int = Field(
        description='An internal, stable identifier that references the location of origin'
    )
    asylum_location_ref: int = Field(
        description='An internal, stable identifier that references the location of asylum'
    )
    population_group: PopulationGroup = Field(description=truncate_query_description(DOC_POPULATION_GROUP))
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
    population: int = Field(ge=0, description='The number of people')
    reference_period_start: NaiveDatetime = Field(description=DOC_REFERENCE_PERIOD_START)
    reference_period_end: Optional[NaiveDatetime] = Field(description=DOC_REFERENCE_PERIOD_END)
    origin_location_code: str = Field(max_length=128, description='Location of origin p-code (ISO-3)')
    origin_location_name: str = Field(max_length=512, description='Location of origin name')

    asylum_location_code: str = Field(max_length=128, description='Location of asylum p-code (ISO-3)')
    asylum_location_name: str = Field(max_length=512, description='Location of asylum name')

    model_config = ConfigDict(from_attributes=True)
