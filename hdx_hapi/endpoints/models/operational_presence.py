from pydantic import ConfigDict, Field, NaiveDatetime
from typing import Optional

from hdx_hapi.endpoints.models.base import HapiBaseModel, HapiModelWithAdmins


class OperationalPresenceResponse(HapiBaseModel, HapiModelWithAdmins):
    # dataset_hdx_stub: str = Field(max_length=128)
    resource_hdx_id: str = Field(max_length=36)
    org_acronym: str = Field(max_length=32)
    org_name: str = Field(max_length=512)
    sector_code: str = Field(
        max_length=32,
        description=(
            'The sector code, derived either from the '
            '[Global Coordination Groups](https://data.humdata.org/dataset/global-coordination-groups-beta?) '
            'dataset, or created for HDX HAPI'
        ),
    )
    sector_name: str = Field(max_length=512, description='The name of the sector')

    reference_period_start: NaiveDatetime
    reference_period_end: Optional[NaiveDatetime]

    # hapi_updated_date: datetime
    # hapi_replaced_date: Optional[datetime]

    # resource_update_date: datetime
    # org_ref: int = None,
    # dataset_hdx_id: str = Field(max_length=36),
    # dataset_title: str = Field(max_length=1024),
    # dataset_hdx_provider_stub: str = Field(max_length=128),
    # dataset_hdx_provider_name: str = Field(max_length=512),
    # resource_name: str = Field(max_length=256),
    org_type_code: Optional[str] = Field(max_length=32, description='The code referring to the organization type')
    org_type_description: Optional[str] = Field(max_length=512, description='A description of the organization type')

    model_config = ConfigDict(from_attributes=True)
