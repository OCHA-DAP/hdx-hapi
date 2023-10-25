from pydantic import ConfigDict, Field, model_validator
from typing import Optional

from hdx_hapi.endpoints.models.base import HapiBaseModel

class OperationalPresenceResponse(HapiBaseModel):

    sector_code: str = Field(max_length=32)
    dataset_hdx_stub: str = Field(max_length=128)
    resource_hdx_id: str = Field(max_length=36)
    org_acronym: str = Field(max_length=32)
    org_name: str = Field(max_length=512)
    sector_name: str = Field(max_length=512)
    location_code: str = Field(max_length=128)
    location_name: str = Field(max_length=512)

    admin1_is_unspecified: bool = Field(exclude=True)
    admin2_is_unspecified: bool = Field(exclude=True)

    admin1_code: Optional[str] = Field(max_length=128)
    admin1_name: Optional[str] = Field(max_length=512)
    admin2_code: Optional[str] = Field(max_length=128)
    admin2_name: Optional[str] = Field(max_length=512)
    # resource_update_date: datetime
    # org_ref: int = None,
    # dataset_hdx_id: str = Field(max_length=36),
    # dataset_title: str = Field(max_length=1024),
    # dataset_hdx_provider_stub: str = Field(max_length=128),
    # dataset_provider_name: str = Field(max_length=512),
    # resource_name: str = Field(max_length=256),
    # org_type_code: str = Field(max_length=32),
    # org_type_description: str = Field(max_length=512),


    model_config = ConfigDict(from_attributes=True)

    @model_validator(mode='after')
    def set_admin1_admin2_null(self) -> 'OperationalPresenceResponse':
        admin1_is_unspecified = self.admin1_is_unspecified
        admin2_is_unspecified = self.admin2_is_unspecified

        # If 'admin1_is_unspecified' is True, set 'admin1_code' and 'admin1_name' to None
        if admin1_is_unspecified:
            self.admin1_code = None
            self.admin1_name = None

        # If 'admin2_is_unspecified' is True, set 'admin2_code' and 'admin2_name' to None
        if admin2_is_unspecified:
            self.admin2_code = None
            self.admin2_name = None

        return self
