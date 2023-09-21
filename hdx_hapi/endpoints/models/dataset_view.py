from pydantic import BaseModel, Field, HttpUrl, computed_field
from typing import Optional
from hdx_hapi.services.hdx_url_logic import get_dataset_url, get_dataset_api_url


class DatasetViewPydantic(BaseModel):
    # id: int
    # code: str = Field(max_length=128)
    hdx_id: str = Field(max_length=36)
    hdx_stub: str = Field(max_length=100)
    title: str = Field(max_length=1024)
    provider_code: str = Field(max_length=128)
    provider_name: str = Field(max_length=512)

    # computed fields

    @computed_field
    @property
    def hdx_link(self) -> HttpUrl:
        return get_dataset_url(dataset_id=self.hdx_id)


    @computed_field
    @property
    def api_link(self) -> HttpUrl:
        return get_dataset_api_url(dataset_id=self.hdx_id)


    class Config:
        orm_mode = True
