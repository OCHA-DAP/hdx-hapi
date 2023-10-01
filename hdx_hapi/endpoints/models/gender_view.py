from pydantic import ConfigDict, Field

from hdx_hapi.endpoints.models.base import HapiBaseModel


class GenderViewPydantic(HapiBaseModel):
    code: str = Field(max_length=1)
    description: str = Field(max_length=256)

    model_config = ConfigDict(from_attributes=True)
