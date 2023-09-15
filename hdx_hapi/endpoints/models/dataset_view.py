from pydantic import BaseModel, Field, computed_field
from typing import Optional
from hdx_hapi.processing.helpers import Context, get_dataset_url, get_dataset_api_url
from hdx_hapi.config.config import get_config

context = Context(config=get_config())

class DatasetViewPydantic(BaseModel):
    # id: int
    code: str = Field(max_length=128)
    title: str = Field(max_length=1024)
    provider_code: str = Field(max_length=128)
    provider_name: str  = Field(max_length=512)

    # computed fields

    @computed_field
    @property
    def hdx_link(self) -> str:
        return get_dataset_url(context=context, dataset_id=self.code)


    @computed_field
    @property
    def api_link(self) -> str:
        return get_dataset_api_url(context=context, dataset_id=self.code)


    class Config:
        orm_mode = True
