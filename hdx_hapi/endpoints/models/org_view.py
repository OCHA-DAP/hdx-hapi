from pydantic import BaseModel, Field, HttpUrl, computed_field
from hdx_hapi.services.hdx_url_logic import get_organization_url


class OrgViewPydantic(BaseModel):
    acronym: str = Field(max_length=32)
    name: str = Field(max_length=512)
    org_type_code: str = Field(max_length=32)
    org_type_description: str = Field(max_length=32)

    @computed_field
    @property
    def hdx_link(self) -> HttpUrl:
        return get_organization_url(org_id=self.acronym)

    class Config:
        orm_mode = True
