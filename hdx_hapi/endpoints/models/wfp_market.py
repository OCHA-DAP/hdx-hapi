from typing import Optional
from pydantic import ConfigDict, Field
from hdx_hapi.endpoints.models.base import HapiBaseModel, HapiModelWithAdmins


class WfpMarketResponse(HapiBaseModel, HapiModelWithAdmins):
    code: str = Field(max_length=32, description='The unique code identifying the market')
    name: str = Field(max_length=512, description='The name of the market')

    lat: Optional[float] = Field(ge=-90.0, le=90.0, description="The market's latitude")
    lon: Optional[float] = Field(ge=-180.0, le=180.0, description="The market's longitude")

    model_config = ConfigDict(from_attributes=True)
