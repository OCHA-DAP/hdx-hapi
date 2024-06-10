from hapi_schema.utils.enums import CommodityCategory
from pydantic import ConfigDict, Field
from hdx_hapi.config.doc_snippets import DOC_COMMODITY_CATEGORY, truncate_query_description
from hdx_hapi.endpoints.models.base import HapiBaseModel


class WfpCommodityResponse(HapiBaseModel):
    code: str = Field(max_length=32, description='The unique code identifying the commodity')
    category: CommodityCategory = Field(description=truncate_query_description(DOC_COMMODITY_CATEGORY))
    name: str = Field(max_length=512, description='The name of the commodity')

    model_config = ConfigDict(from_attributes=True)
