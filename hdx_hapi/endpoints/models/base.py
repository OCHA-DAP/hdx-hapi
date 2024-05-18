from typing import Generic, List, Optional, TypeVar
from typing_extensions import Self
from pydantic import BaseModel, ConfigDict, Field, model_validator


class HapiBaseModel(BaseModel):
    def list_of_fields(self) -> List[str]:
        return list(self.model_fields.keys())


class HapiModelWithAdmins(BaseModel):
    location_ref: int
    location_code: str = Field(max_length=128)
    location_name: str = Field(max_length=512)

    admin1_is_unspecified: bool = Field(exclude=True)
    admin2_is_unspecified: bool = Field(exclude=True)

    admin1_ref: int
    admin1_code: Optional[str] = Field(max_length=128)
    admin1_name: Optional[str] = Field(max_length=512)
    admin2_ref: int
    admin2_code: Optional[str] = Field(max_length=128)
    admin2_name: Optional[str] = Field(max_length=512)

    @model_validator(mode='after')  # type: ignore
    def set_admin1_admin2_null(self) -> Self:
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


DataT = TypeVar('DataT')


class HapiGenericResponse(BaseModel, Generic[DataT]):
    data: List[DataT]

    model_config = ConfigDict(from_attributes=True)
