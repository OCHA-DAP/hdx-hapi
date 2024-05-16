from typing import List
from datetime import datetime
from pydantic import ConfigDict, Field, HttpUrl, computed_field
from hdx_hapi.endpoints.models.base import HapiBaseModel
from hdx_hapi.services.hdx_url_logic import (
    get_resource_url,
    get_resource_api_url,
    get_dataset_url,
    get_dataset_api_url,
    get_organization_url,
)


class DatasetResponse(HapiBaseModel):
    hdx_id: str = Field(max_length=36)
    hdx_stub: str = Field(max_length=128)
    title: str = Field(max_length=1024)
    hdx_provider_stub: str = Field(max_length=128)
    hdx_provider_name: str = Field(max_length=512)

    # computed fields

    @computed_field
    @property
    def hdx_link(self) -> HttpUrl:
        return get_dataset_url(dataset_id=self.hdx_id)

    @computed_field
    @property
    def hdx_api_link(self) -> HttpUrl:
        return get_dataset_api_url(dataset_id=self.hdx_id)

    @computed_field
    @property
    def provider_hdx_link(self) -> HttpUrl:
        return get_organization_url(org_id=self.hdx_provider_stub)

    model_config = ConfigDict(from_attributes=True)

    def list_of_fields(self) -> List[str]:
        fields = super().list_of_fields()
        fields.extend(['hdx_link', 'api_link', 'hdx_provider_link'])
        return fields


class ResourceResponse(HapiBaseModel):
    # id: int
    hdx_id: str = Field(max_length=36)
    dataset_hdx_id: str = Field(max_length=36)
    name: str = Field(max_length=256)
    format: str = Field(max_length=32)
    update_date: datetime
    is_hxl: bool
    download_url: HttpUrl
    hapi_updated_date: datetime

    dataset_hdx_stub: str = Field(max_length=128)

    dataset_title: str = Field(max_length=1024)
    dataset_hdx_provider_stub: str = Field(max_length=128)
    dataset_hdx_provider_name: str = Field(max_length=512)

    # computed fields

    @computed_field
    @property
    def hdx_link(self) -> HttpUrl:
        return get_resource_url(dataset_id=self.dataset_hdx_id, resource_id=self.hdx_id)

    @computed_field
    @property
    def hdx_api_link(self) -> HttpUrl:
        return get_resource_api_url(resource_id=self.hdx_id)

    @computed_field
    @property
    def dataset_hdx_link(self) -> HttpUrl:
        return get_dataset_url(dataset_id=self.dataset_hdx_id)

    @computed_field
    @property
    def dataset_hdx_api_link(self) -> HttpUrl:
        return get_dataset_api_url(dataset_id=self.dataset_hdx_id)

    @computed_field
    @property
    def provider_hdx_link(self) -> HttpUrl:
        return get_organization_url(org_id=self.dataset_hdx_provider_stub)

    model_config = ConfigDict(from_attributes=True)

    def list_of_fields(self) -> List[str]:
        fields = super().list_of_fields()
        fields.extend(['hdx_link', 'api_link', 'dataset_hdx_link', 'dataset_api_link'])
        return fields
