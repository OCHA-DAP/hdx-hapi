from pydantic import ConfigDict, Field

from hdx_hapi.endpoints.models.base import HapiBaseModel

class LocationViewPydantic(HapiBaseModel):
    # id: int
    code: str = Field(max_length=128)
    name: str = Field(max_length=512)

    model_config = ConfigDict(from_attributes=True)
