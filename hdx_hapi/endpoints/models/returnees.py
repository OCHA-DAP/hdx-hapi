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
    truncate_query_description,
)
from hdx_hapi.endpoints.models.base import HapiBaseModel


class ReturneesResponse(HapiBaseModel):
    resource_hdx_id: str = Field(max_length=36, description=truncate_query_description(DOC_HDX_RESOURCE_ID))
    origin_location_ref: int = Field(description='Placeholder text')
    asylum_location_ref: int = Field(description='Placeholder text')
    population_group: PopulationGroup = Field(description=truncate_query_description(DOC_POPULATION_GROUP))
    gender: Gender = Field(description=truncate_query_description(DOC_GENDER))
    age_range: str = Field(max_length=32, description='Placeholder text')
    min_age: int = Field(description='Placeholder text')
    max_age: int = Field(description='Placeholder text')
    population: int = Field(description='Placeholder text')
    reference_period_start: datetime.datetime = Field(
        description=truncate_query_description(DOC_REFERENCE_PERIOD_START)
    )
    reference_period_end: Optional[datetime.datetime] = Field(
        description=truncate_query_description(DOC_REFERENCE_PERIOD_END)
    )
    origin_location_code: str = Field(max_length=128, description='Placeholder text')
    origin_location_name: str = Field(max_length=512, description='Placeholder text')
    asylum_location_code: str = Field(max_length=128, description='Placeholder text')
    asylum_location_name: str = Field(max_length=512, description='Placeholder text')

    model_config = ConfigDict(from_attributes=True)
