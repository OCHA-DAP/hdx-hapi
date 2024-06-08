from typing import List
from datetime import datetime
from pydantic import ConfigDict, Field, HttpUrl, computed_field
from hdx_hapi.config.doc_snippets import (
    DOC_HDX_DATASET_IN_RESOURCE_NAME,
    DOC_HDX_DATASET_STUB,
    DOC_HDX_DATASET_TITLE,
    DOC_HDX_PROVIDER_IN_RESOURCE_STUB,
    DOC_HDX_PROVIDER_NAME,
    DOC_HDX_PROVIDER_STUB,
    DOC_HDX_RESOURCE_ID,
    DOC_HDX_DATASET_ID,
    DOC_HDX_RESOURCE_FORMAT,
    DOC_HDX_RESOURCE_HXL,
    truncate_query_description,
)
from hdx_hapi.endpoints.models.base import HapiBaseModel
from hdx_hapi.services.hdx_url_logic import (
    get_resource_url,
    get_resource_api_url,
    get_dataset_url,
    get_dataset_api_url,
    get_organization_url,
    get_organization_api_url,
)


class DatasetResponse(HapiBaseModel):
    dataset_hdx_id: str = Field(max_length=36, description=truncate_query_description(DOC_HDX_DATASET_ID))
    dataset_hdx_stub: str = Field(max_length=128, description=truncate_query_description(DOC_HDX_DATASET_STUB))
    dataset_hdx_title: str = Field(max_length=1024, description=truncate_query_description(DOC_HDX_DATASET_TITLE))
    hdx_provider_stub: str = Field(max_length=128, description=truncate_query_description(DOC_HDX_PROVIDER_STUB))
    hdx_provider_name: str = Field(max_length=512, description=truncate_query_description(DOC_HDX_PROVIDER_NAME))

    # computed fields

    @computed_field
    @property
    def hdx_link(self) -> HttpUrl:
        return get_dataset_url(dataset_id=self.dataset_hdx_id)

    @computed_field
    @property
    def hdx_api_link(self) -> HttpUrl:
        return get_dataset_api_url(dataset_id=self.dataset_hdx_id)

    @computed_field
    @property
    def provider_hdx_link(self) -> HttpUrl:
        return get_organization_url(org_id=self.hdx_provider_stub)

    model_config = ConfigDict(from_attributes=True)

    @computed_field
    @property
    def provider_hdx_api_link(self) -> HttpUrl:
        return get_organization_api_url(org_id=self.hdx_provider_stub)

    model_config = ConfigDict(from_attributes=True)

    def list_of_fields(self) -> List[str]:
        fields = super().list_of_fields()
        fields.extend(['hdx_link', 'api_link', 'provider_hdx_link', 'provider_hdx_api_link'])
        return fields


class ResourceResponse(HapiBaseModel):
    # id: int
    resource_hdx_id: str = Field(max_length=36, description=truncate_query_description(DOC_HDX_RESOURCE_ID))
    dataset_hdx_id: str = Field(max_length=36, description=truncate_query_description(DOC_HDX_DATASET_ID))
    name: str = Field(
        max_length=256,
        description=(
            'The resource name on HDX. In combination with the dataset UUIDs'
            'from the `dataset_hdx_id` and `resource_hdx_id` fields respectively, it can be used to '
            'construct a URL to download the resource: '
            '`https://data.humdata.org/dataset/[dataset_hdx_id]/resource/[resource_hdx_id]/download/[name]`, '
            'which can be found in the `download_url` field.'
        ),
    )
    format: str = Field(max_length=32, description=truncate_query_description(DOC_HDX_RESOURCE_FORMAT))
    update_date: datetime = Field(description='The date the resource was last updated')
    is_hxl: bool = Field(description=truncate_query_description(DOC_HDX_RESOURCE_HXL))
    download_url: HttpUrl = Field(
        description='A URL to directly download the resource file from HDX, in the format '
        'specified in the `format` field.'
    )
    hapi_updated_date: datetime = Field(description='The date that the resource was ingested into HDX HAPI')

    dataset_hdx_stub: str = Field(max_length=128, description=truncate_query_description(DOC_HDX_DATASET_STUB))

    dataset_hdx_title: str = Field(max_length=1024, description=truncate_query_description(DOC_HDX_DATASET_TITLE))
    dataset_hdx_provider_stub: str = Field(max_length=128, description=DOC_HDX_PROVIDER_IN_RESOURCE_STUB)
    dataset_hdx_provider_name: str = Field(max_length=512, description=DOC_HDX_PROVIDER_NAME)

    # computed fields

    @computed_field
    @property
    def hdx_link(self) -> HttpUrl:
        return get_resource_url(dataset_id=self.dataset_hdx_id, resource_id=self.resource_hdx_id)

    @computed_field
    @property
    def hdx_api_link(self) -> HttpUrl:
        return get_resource_api_url(resource_id=self.resource_hdx_id)

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

    @computed_field
    @property
    def provider_hdx_api_link(self) -> HttpUrl:
        return get_organization_api_url(org_id=self.dataset_hdx_provider_stub)

    model_config = ConfigDict(from_attributes=True)

    def list_of_fields(self) -> List[str]:
        fields = super().list_of_fields()
        fields.extend(['hdx_link', 'api_link', 'dataset_hdx_link', 'dataset_hdx_api_link'])
        return fields
