from pydantic import BaseModel, Field
from pydantic.functional_validators import field_validator
from typing import Optional
from datetime import datetime
from config.config import get_config
from hdx_hapi.helpers import Context, get_dataset_url

context = Context(config=get_config())

class OrgViewPydantic(BaseModel):
    # id: int
    hdx_link: str = Field(max_length=1024)
    acronym: str = Field(max_length=32)
    name: str = Field(max_length=512)
    # org_type_code: str = Field(max_length=32)
    reference_period_start: datetime
    reference_period_end: Optional[datetime]

    @field_validator('hdx_link')
    @classmethod
    def create_url(cls, v) -> str:
        return get_dataset_url(context=context, dataset_name=v)

    class Config:
        orm_mode = True
