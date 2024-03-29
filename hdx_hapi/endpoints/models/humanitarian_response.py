from pydantic import ConfigDict, Field
from typing import Optional
from hdx_hapi.endpoints.models.base import HapiBaseModel


class OrgResponse(HapiBaseModel):
    # id: int
    # hdx_link: str = Field(max_length=1024)
    acronym: str = Field(max_length=32)
    name: str = Field(max_length=512)
    org_type_code: Optional[str] = Field(max_length=32)
    org_type_description: Optional[str] = Field(max_length=32)

    # @computed_field
    # @property
    # def hdx_link(self) -> HttpUrl:
    #     return get_organization_url(org_id=self.acronym)

    model_config = ConfigDict(from_attributes=True)

    # def list_of_fields(self) -> List[str]:
    #     fields = super().list_of_fields()
    #     fields.extend(['hdx_link'])
    #     return fields


class OrgTypeResponse(HapiBaseModel):
    code: str = Field(max_length=32)
    description: str = Field(max_length=512)

    model_config = ConfigDict(from_attributes=True)


class SectorResponse(HapiBaseModel):
    code: str = Field(max_length=32)
    name: str = Field(max_length=512)

    model_config = ConfigDict(from_attributes=True)
