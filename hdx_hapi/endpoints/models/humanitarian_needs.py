import datetime
from pydantic import ConfigDict, Field
from typing import Optional

from hdx_hapi.config.doc_snippets import (
    DOC_DISABLED_MARKER,
    DOC_GENDER,
    DOC_POPULATION_GROUP,
    DOC_POPULATION_STATUS,
    DOC_HDX_RESOURCE_ID,
    DOC_AGE_RANGE,
    DOC_REFERENCE_PERIOD_START,
    DOC_REFERENCE_PERIOD_END,
    truncate_query_description,
)
from hdx_hapi.endpoints.models.base import HapiBaseModel, HapiModelWithAdmins
from hapi_schema.utils.enums import Gender, PopulationGroup, PopulationStatus, DisabledMarker


class HumanitarianNeedsResponse(HapiBaseModel, HapiModelWithAdmins):
    resource_hdx_id: str = Field(max_length=36, description=truncate_query_description(DOC_HDX_RESOURCE_ID))
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
    disabled_marker: DisabledMarker = Field(description=truncate_query_description(DOC_DISABLED_MARKER))
    sector_code: str = Field(
        max_length=32,
        description=(
            'The sector code, derived either from the '
            '[Global Coordination Groups](https://data.humdata.org/dataset/global-coordination-groups-beta?) '
            'dataset, or created for HDX HAPI'
        ),
    )
    population_group: PopulationGroup = Field(description=truncate_query_description(DOC_POPULATION_GROUP))
    population_status: PopulationStatus = Field(description=truncate_query_description(DOC_POPULATION_STATUS))
    population: int = Field(ge=0, description='The number of people')
    reference_period_start: datetime.datetime = Field(description=DOC_REFERENCE_PERIOD_START)
    reference_period_end: Optional[datetime.datetime] = Field(description=DOC_REFERENCE_PERIOD_END)
    sector_name: Optional[str] = Field(max_length=512, description='The name of the sector')

    model_config = ConfigDict(from_attributes=True)
