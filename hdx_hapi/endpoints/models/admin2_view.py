from pydantic import ConfigDict, Field
from typing import Optional
from datetime import datetime

from hdx_hapi.endpoints.models.base import HapiBaseModel


class Admin2ViewPydantic(HapiBaseModel):
    # id: int
    # admin1_ref: int
    code: str = Field(max_length=128)
    name: str = Field(max_length=512)
    is_unspecified: bool
    reference_period_start: datetime
    reference_period_end: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)
