from datetime import datetime
from pydantic import BaseModel, Field, HttpUrl, computed_field
from typing import Annotated, Optional

from sqlalchemy import Boolean
from hdx_hapi.services.hdx_url_logic import (
    get_resource_url,
    get_resource_api_url,
    get_dataset_url,
    get_dataset_api_url,
)


class ResourceViewPydantic(BaseModel):
    # id: int
    hdx_id: str = Field(max_length=36)
    filename: str = Field(max_length=256)
    format: str = Field(max_length=32)
    update_date: datetime
    is_hxl: bool
    download_url: str = Field(max_length=1024)

    dataset_hdx_id: str = Field(max_length=36)
    dataset_hdx_stub: str = Field(max_length=128)
    
    dataset_title: str = Field(max_length=1024) 
    dataset_provider_code: str = Field(max_length=128)
    dataset_provider_name: str = Field(max_length=512)


    # computed fields

    @computed_field
    @property
    def hdx_link(self) -> HttpUrl:
        return get_resource_url(dataset_id=self.dataset_hdx_id, resource_id=self.hdx_id)

    @computed_field
    @property
    def api_link(self) -> HttpUrl:
        return get_resource_api_url(resource_id=self.hdx_id)

    @computed_field
    @property
    def dataset_hdx_link(self) -> HttpUrl:
        return get_dataset_url(dataset_id=self.dataset_hdx_id)

    @computed_field
    @property
    def dataset_api_link(self) -> HttpUrl:
        return get_dataset_api_url(dataset_id=self.dataset_hdx_id)

    class Config:
        orm_mode = True
