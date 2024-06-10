from pydantic import Field
from hdx_hapi.endpoints.models.base import HapiBaseModel


class IdentifierResponse(HapiBaseModel):
    encoded_app_identifier: str = Field(
        max_length=512, description='Base64 encoded app_identifier compiled from application name and email address'
    )
