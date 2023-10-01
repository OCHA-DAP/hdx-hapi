from pydantic import ConfigDict, Field
from typing import Optional
from datetime import datetime

from hdx_hapi.endpoints.models.base import HapiBaseModel


class LocationViewPydantic(HapiBaseModel):
    # id: int
    code: str = Field(max_length=128)
    name: str = Field(max_length=512)
    reference_period_start: datetime
    reference_period_end: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)
