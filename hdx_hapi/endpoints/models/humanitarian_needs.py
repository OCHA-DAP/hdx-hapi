import datetime
from pydantic import ConfigDict, Field
from typing import Optional

from hdx_hapi.config.doc_snippets import (
    DOC_POPULATION_STATUS,
    DOC_HDX_RESOURCE_ID,
    DOC_REFERENCE_PERIOD_START,
    DOC_REFERENCE_PERIOD_END,
    truncate_query_description,
)
from hdx_hapi.endpoints.models.base import HapiBaseModel, HapiModelWithAdmins
from hapi_schema.utils.enums import PopulationStatus


class HumanitarianNeedsResponse(HapiBaseModel, HapiModelWithAdmins):
    resource_hdx_id: str = Field(max_length=36, description=truncate_query_description(DOC_HDX_RESOURCE_ID))
    sector_code: str = Field(
        max_length=32,
        description=(
            'The sector code, derived either from the '
            '[Global Coordination Groups](https://data.humdata.org/dataset/global-coordination-groups-beta?) '
            'dataset, or created for HDX HAPI'
        ),
    )
    category: str = Field(
        max_length=128,
        description='A category combining gender, age range, disability marker and population group information',
    )
    population_status: PopulationStatus = Field(description=truncate_query_description(DOC_POPULATION_STATUS))
    population: int = Field(ge=0, description='The number of people')
    reference_period_start: datetime.datetime = Field(description=DOC_REFERENCE_PERIOD_START)
    reference_period_end: Optional[datetime.datetime] = Field(description=DOC_REFERENCE_PERIOD_END)
    sector_name: Optional[str] = Field(max_length=512, description='The name of the sector')

    model_config = ConfigDict(from_attributes=True)
