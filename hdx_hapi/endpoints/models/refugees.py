from pydantic import ConfigDict, Field, NaiveDatetime
from typing import Optional

from hdx_hapi.config.doc_snippets import DOC_GENDER, DOC_POPULATION_GROUP, truncate_query_description
from hdx_hapi.endpoints.models.base import HapiBaseModel
from hapi_schema.utils.enums import Gender, PopulationGroup


class RefugeesResponse(HapiBaseModel):
    resource_hdx_id: str = Field(max_length=36)
    origin_location_ref: int
    asylum_location_ref: int
    population_group: PopulationGroup = Field(description=truncate_query_description(DOC_POPULATION_GROUP))
    gender: Gender = Field(description=truncate_query_description(DOC_GENDER))
    age_range: str = Field(max_length=32)
    min_age: Optional[int] = Field(ge=0)
    max_age: Optional[int] = Field(ge=0)
    population: int = Field(ge=0)
    reference_period_start: NaiveDatetime
    reference_period_end: Optional[NaiveDatetime]
    origin_location_code: str = Field(max_length=128)
    origin_location_name: str = Field(max_length=512)
    asylum_location_code: str = Field(max_length=128)
    asylum_location_name: str = Field(max_length=512)

    model_config = ConfigDict(from_attributes=True)
