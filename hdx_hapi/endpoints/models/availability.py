from pydantic import ConfigDict, Field
from hdx_hapi.endpoints.models.base import HapiBaseModel, HapiModelWithAdmins


class AvailabilityResponse(HapiBaseModel, HapiModelWithAdmins):
    category: str = Field(max_length=32, description='HAPI category')
    subcategory: str = Field(max_length=512, description='HAPI subcategory')

    model_config = ConfigDict(from_attributes=True)
