from pydantic import ConfigDict, Field, validator
from typing import Optional

from hdx_hapi.endpoints.models.base import HapiBaseModel


class PopulationViewPydantic(HapiBaseModel):
    gender_code: Optional[str] = Field(max_length=1)
    age_range_code: Optional[str] = Field(max_length=32)
    population: int
    dataset_hdx_stub: str = Field(max_length=128)
    resource_hdx_id: str = Field(max_length=36)
    location_code: str = Field(max_length=128)
    location_name: str = Field(max_length=512)

    admin1_is_unspecified: bool = Field(exclude=True)
    admin2_is_unspecified: bool = Field(exclude=True)

    admin1_code: Optional[str] = Field(max_length=128)
    admin1_name: Optional[str] = Field(max_length=512)
    admin2_code: Optional[str] = Field(max_length=128)
    admin2_name: Optional[str] = Field(max_length=512)

    model_config = ConfigDict(from_attributes=True)

    @validator('admin1_code', 'admin1_name', pre=True)
    def set_admin1_null(cls, v, values):
        admin1_is_unspecified = values.get('admin1_is_unspecified', False)

        # If 'admin1_is_unspecified' is True, set 'admin1_code' and 'admin1_name' to None
        if admin1_is_unspecified:
            return None

        # If 'admin1_is_unspecified' is False, leave 'admin1_code' and 'admin1_name' unchanged
        return v

    @validator('admin2_code', 'admin2_name', pre=True)
    def set_admin2_null(cls, v, values):
        admin2_is_unspecified = values.get('admin2_is_unspecified', False)

        # If 'admin2_is_unspecified' is True, set 'admin2_code' and 'admin2_name' to None
        if admin2_is_unspecified:
            return None

        # If 'admin2_is_unspecified' is False, leave 'admin2_code' and 'admin2_name' unchanged
        return v
