from pydantic import ConfigDict, Field
from typing import Optional
from datetime import datetime

from hdx_hapi.endpoints.models.base import HapiBaseModel


class Admin2ViewPydantic(HapiBaseModel):
    # id: int
    # admin1_ref: int
    code: str = Field(max_length=128)
    name: str = Field(max_length=512)

    admin1_code: str = Field(max_length=128)
    admin1_name: str = Field(max_length=512)

    location_code: str = Field(max_length=128)
    location_name: str = Field(max_length=512)

    model_config = ConfigDict(from_attributes=True)
