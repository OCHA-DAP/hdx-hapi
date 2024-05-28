from pydantic import ConfigDict, Field, NaiveDatetime
from typing import Optional

from hdx_hapi.endpoints.models.base import HapiBaseModel, HapiModelWithAdmins


class OperationalPresenceResponse(HapiBaseModel, HapiModelWithAdmins):
    # dataset_hdx_stub: str = Field(max_length=128)
    resource_hdx_id: str = Field(max_length=36)
    org_acronym: str = Field(max_length=32)
    org_name: str = Field(max_length=512)
    sector_code: str = Field(max_length=32)
    sector_name: str = Field(max_length=512)

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
    org_type_code: Optional[str] = Field(max_length=32)
    # org_type_description: str = Field(max_length=512),

    model_config = ConfigDict(from_attributes=True)
