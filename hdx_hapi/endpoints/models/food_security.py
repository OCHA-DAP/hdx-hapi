from pydantic import ConfigDict, Field, model_validator, NaiveDatetime
from typing import Optional

from hdx_hapi.endpoints.models.base import HapiBaseModel


class FoodSecurityResponse(HapiBaseModel):
    population_in_phase: int
    population_fraction_in_phase: float

    ipc_phase_code: str = Field(max_length=32)
    ipc_phase_name: str = Field(max_length=32)
    ipc_type_code: str = Field(max_length=32)
    
    reference_period_start: Optional[NaiveDatetime]
    reference_period_end: Optional[NaiveDatetime]

    dataset_hdx_stub: str = Field(max_length=128)
    dataset_hdx_provider_stub: str = Field(max_length=128)
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

    @model_validator(mode='after')
    def set_admin1_admin2_null(self) -> 'FoodSecurityResponse':
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
