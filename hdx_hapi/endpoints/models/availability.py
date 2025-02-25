import datetime
from typing import Optional
from pydantic import ConfigDict, Field
from hdx_hapi.endpoints.models.base import HapiBaseModel, HapiModelWithAdmins


class AvailabilityResponse(HapiBaseModel, HapiModelWithAdmins):
    category: str = Field(max_length=32, description='HAPI category')
    subcategory: str = Field(max_length=512, description='HAPI subcategory')
    hapi_updated_date: Optional[datetime.datetime] = Field(
        description='Date that dataset was last updated, e.g. 2020-01-01 or 2020-01-01T00:00:00'
    )

    model_config = ConfigDict(from_attributes=True)
