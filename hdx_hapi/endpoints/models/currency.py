from pydantic import ConfigDict, Field
from hdx_hapi.endpoints.models.base import HapiBaseModel


class CurrencyResponse(HapiBaseModel):
    code: str = Field(max_length=32)
    name: str = Field(max_length=512)

    model_config = ConfigDict(from_attributes=True)
