from decimal import Decimal
from typing import Optional
from hapi_schema.utils.enums import CommodityCategory, PriceFlag, PriceType
from pydantic import ConfigDict, Field, NaiveDatetime
from hdx_hapi.endpoints.models.base import HapiBaseModel, HapiModelWithAdmins


class FoodPriceResponse(HapiBaseModel, HapiModelWithAdmins):
    resource_hdx_id: str = Field(max_length=36)

    market_code: str = Field(max_length=32)
    market_name: str = Field(max_length=512)
    commodity_code: str = Field(max_length=32)
    commodity_name: str = Field(max_length=512)
    commodity_category: CommodityCategory

    currency_code: str = Field(max_length=32)
    unit: str = Field(max_length=32)

    price_flag: PriceFlag
    price_type: PriceType
    price: Decimal

    lat: float = Field(ge=-90.0, le=90.0)
    lon: float = Field(ge=-180.0, le=180.0)

    reference_period_start: NaiveDatetime
    reference_period_end: Optional[NaiveDatetime]

    model_config = ConfigDict(from_attributes=True)
