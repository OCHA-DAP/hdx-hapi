from pydantic import Field
from hdx_hapi.endpoints.models.base import HapiBaseModel


class IdentifierResponse(HapiBaseModel):
    encoded_identifier: str = Field(max_length=512)
