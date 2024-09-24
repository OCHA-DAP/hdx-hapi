import datetime
from hapi_schema.utils.enums import PopulationGroup, Gender
from pydantic import ConfigDict, Field
from typing import Optional

from hdx_hapi.config.doc_snippets import (
    DOC_GENDER,
    DOC_POPULATION_GROUP,
    DOC_HDX_RESOURCE_ID,
    DOC_REFERENCE_PERIOD_START,
    DOC_REFERENCE_PERIOD_END,
    DOC_LOCATION_REF,
    DOC_AGE_RANGE,
    DOC_LOCATION_NAME,
    DOC_LOCATION_CODE,
    truncate_query_description,
)
from hdx_hapi.endpoints.models.base import HapiBaseModel


class ReturneesResponse(HapiBaseModel):
    resource_hdx_id: str = Field(max_length=36, description=truncate_query_description(DOC_HDX_RESOURCE_ID))
    origin_location_ref: int = Field(description=truncate_query_description(DOC_LOCATION_REF))
    asylum_location_ref: int = Field(description=truncate_query_description(DOC_LOCATION_REF))
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
    reference_period_start: datetime.datetime = Field(
        description=truncate_query_description(DOC_REFERENCE_PERIOD_START)
    )
    reference_period_end: Optional[datetime.datetime] = Field(
        description=truncate_query_description(DOC_REFERENCE_PERIOD_END)
    )
    origin_location_code: str = Field(max_length=128, description=truncate_query_description(DOC_LOCATION_CODE))
    origin_location_name: str = Field(max_length=512, description=truncate_query_description(DOC_LOCATION_NAME))
    asylum_location_code: str = Field(max_length=128, description=truncate_query_description(DOC_LOCATION_CODE))
    asylum_location_name: str = Field(max_length=512, description=truncate_query_description(DOC_LOCATION_NAME))

    model_config = ConfigDict(from_attributes=True)
