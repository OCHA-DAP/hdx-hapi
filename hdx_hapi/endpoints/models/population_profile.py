from pydantic import ConfigDict, Field

from hdx_hapi.endpoints.models.base import HapiBaseModel


class PopulationGroupResponse(HapiBaseModel):
    code: str = Field(max_length=32)
    description: str = Field(max_length=512)

    model_config = ConfigDict(from_attributes=True)


class PopulationStatusResponse(HapiBaseModel):
    code: str = Field(max_length=32)
    description: str = Field(max_length=512)

    model_config = ConfigDict(from_attributes=True)
