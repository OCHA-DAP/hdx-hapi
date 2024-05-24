from hapi_schema.utils.enums import CommodityCategory
from pydantic import ConfigDict, Field
from hdx_hapi.endpoints.models.base import HapiBaseModel


class WfpCommodityResponse(HapiBaseModel):
    code: str = Field(max_length=32)
    category: CommodityCategory
    name: str = Field(max_length=512)

    model_config = ConfigDict(from_attributes=True)
