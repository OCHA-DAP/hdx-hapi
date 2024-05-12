from datetime import datetime
from typing import Optional
from pydantic import ConfigDict, Field
from hdx_hapi.endpoints.models.base import HapiBaseModel


class LocationResponse(HapiBaseModel):
    # id: int
    code: str = Field(max_length=128)
    name: str = Field(max_length=512)

    model_config = ConfigDict(from_attributes=True)


class Admin1Response(HapiBaseModel):
    # id: int
    # location_ref: int
    code: str = Field(max_length=128)
    name: str = Field(max_length=512)
    hapi_updated_date: datetime
    hapi_replaced_date: Optional[datetime]
    location_code: str = Field(max_length=128)
    location_name: str = Field(max_length=512)

    model_config = ConfigDict(from_attributes=True)


class Admin2Response(HapiBaseModel):
    # id: int
    # admin1_ref: int
    code: str = Field(max_length=128)
    name: str = Field(max_length=512)
    hapi_updated_date: datetime
    hapi_replaced_date: Optional[datetime]

    admin1_code: str = Field(max_length=128)
    admin1_name: str = Field(max_length=512)

    location_code: str = Field(max_length=128)
    location_name: str = Field(max_length=512)

    model_config = ConfigDict(from_attributes=True)
