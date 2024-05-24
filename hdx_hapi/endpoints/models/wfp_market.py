from pydantic import ConfigDict, Field
from hdx_hapi.endpoints.models.base import HapiBaseModel, HapiModelWithAdmins


class WfpMarketResponse(HapiBaseModel, HapiModelWithAdmins):
    code: str = Field(max_length=32)
    name: str = Field(max_length=512)

    lat: float = Field(ge=-90.0, le=90.0)
    lon: float = Field(ge=-180.0, le=180.0)

    model_config = ConfigDict(from_attributes=True)
