from pydantic import ConfigDict, Field
from typing import Optional
from hdx_hapi.endpoints.models.base import HapiBaseModel


class OrgResponse(HapiBaseModel):
    # id: int
    # hdx_link: str = Field(max_length=1024)
    acronym: str = Field(max_length=32, description='The organization acronym')
    name: str = Field(max_length=512, description='The organization name')
    org_type_code: Optional[str] = Field(max_length=32, description='The code referring to the organization type')
    org_type_description: Optional[str] = Field(max_length=32, description='A description of the organization type')

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
    code: str = Field(
        max_length=32,
        description=(
            ' The code referring to the organization type, derived either from the '
            '[OCHA Digital Services organization types list](https://data.humdata.org/dataset/organization-types-beta),'
            ' or created for HDX HAPI'
        ),
    )
    description: str = Field(max_length=512, description='A description of the organization type')

    model_config = ConfigDict(from_attributes=True)


class SectorResponse(HapiBaseModel):
    code: str = Field(
        max_length=32,
        description=(
            'The sector code, derived either from the '
            '[Global Coordination Groups](https://data.humdata.org/dataset/global-coordination-groups-beta?) '
            'dataset, or created for HDX HAPI'
        ),
    )
    name: str = Field(max_length=512, description='The name of the sector')

    model_config = ConfigDict(from_attributes=True)
