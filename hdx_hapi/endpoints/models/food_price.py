from typing import Optional
from pydantic import ConfigDict, Field, NaiveDatetime
from hapi_schema.utils.enums import CommodityCategory, PriceFlag, PriceType
from hdx_hapi.config.doc_snippets import DOC_REFERENCE_PERIOD_END, DOC_REFERENCE_PERIOD_START
from hdx_hapi.endpoints.models.base import HapiBaseModel, HapiModelWithAdmins
from hdx_hapi.endpoints.models.util.constants import NON_NEGATIVE_DECIMAL_TYPE


class FoodPriceResponse(HapiBaseModel, HapiModelWithAdmins):
    resource_hdx_id: str = Field(max_length=36, description='Unique resource UUID on HDX')

    market_code: str = Field(max_length=32, description='The unique code identifying the market')
    market_name: str = Field(max_length=512, description='The name of the market')
    commodity_code: str = Field(max_length=32, description='The unique code identifying the commodity')
    commodity_name: str = Field(max_length=512, description='The name of the commodity')
    commodity_category: CommodityCategory = Field(description='The food group that the commodity belongs to')

    currency_code: str = Field(max_length=32, description='ISO-4217 currency code')
    unit: str = Field(max_length=32, description='The unit of the commodity, such as weight or number')

    price_flag: PriceFlag = Field(description='Pre-processing characteristics of food price')
    price_type: PriceType = Field(description='The point in the supply chain at which the price is determined')
    price: NON_NEGATIVE_DECIMAL_TYPE
    lat: float = Field(ge=-90.0, le=90.0, description="The market's latitude")
    lon: float = Field(ge=-180.0, le=180.0, description="The market's longitude")

    reference_period_start: NaiveDatetime = Field(description=DOC_REFERENCE_PERIOD_START)
    reference_period_end: Optional[NaiveDatetime] = Field(description=DOC_REFERENCE_PERIOD_END)

    model_config = ConfigDict(from_attributes=True)
