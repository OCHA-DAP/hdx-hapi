from pydantic import ConfigDict, Field
from hdx_hapi.endpoints.models.base import HapiBaseModel


class CurrencyResponse(HapiBaseModel):
    code: str = Field(max_length=32, description='ISO-4217 currency code')
    name: str = Field(max_length=512, description='Currency name')

    model_config = ConfigDict(from_attributes=True)
