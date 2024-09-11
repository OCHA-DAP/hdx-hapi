import datetime

from pydantic import ConfigDict, Field
from typing import Optional

from hdx_hapi.config.doc_snippets import (
    DOC_HDX_RESOURCE_ID,
    DOC_REFERENCE_PERIOD_END,
    DOC_REFERENCE_PERIOD_START,
    truncate_query_description,
)
from hdx_hapi.endpoints.models.base import HapiBaseModel, HapiModelWithAdmins


class OperationalPresenceResponse(HapiBaseModel, HapiModelWithAdmins):
    # dataset_hdx_stub: str = Field(max_length=128)
    resource_hdx_id: str = Field(max_length=36, description=truncate_query_description(DOC_HDX_RESOURCE_ID))
    org_acronym: str = Field(max_length=32, description='The organization acronym')
    org_name: str = Field(max_length=512, description='The organization name')
    sector_code: str = Field(
        max_length=32,
        description=(
            'The sector code, derived either from the '
            '[Global Coordination Groups](https://data.humdata.org/dataset/global-coordination-groups-beta?) '
            'dataset, or created for HDX HAPI'
        ),
    )
    sector_name: str = Field(max_length=512, description='The name of the sector')

    reference_period_start: datetime.datetime = Field(description=DOC_REFERENCE_PERIOD_START)
    reference_period_end: Optional[datetime.datetime] = Field(description=DOC_REFERENCE_PERIOD_END)

    org_type_code: Optional[str] = Field(max_length=32, description='The code referring to the organization type')
    org_type_description: Optional[str] = Field(max_length=512, description='A description of the organization type')

    model_config = ConfigDict(from_attributes=True)
