from pydantic import Field
from hdx_hapi.endpoints.models.base import HapiBaseModel


class VersionResponse(HapiBaseModel):
    api_version: str = Field(max_length=16)
    hapi_sqlalchemy_schema_version: str = Field(max_length=16)
