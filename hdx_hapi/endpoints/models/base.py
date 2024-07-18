from typing import Generic, List, Optional, TypeVar
from typing_extensions import Self
from pydantic import BaseModel, ConfigDict, Field, model_validator

from hdx_hapi.config.doc_snippets import (
    DOC_LOCATION_CODE,
    DOC_LOCATION_REF,
    DOC_LOCATION_NAME,
    DOC_LOCATION_HAS_HRP,
    DOC_LOCATION_IN_GHO,
    DOC_ADMIN1_REF,
    DOC_ADMIN1_NAME,
    DOC_ADMIN1_CODE,
    DOC_ADMIN2_REF,
    DOC_ADMIN2_NAME,
    DOC_ADMIN2_CODE,
    truncate_query_description,
)


class HapiBaseModel(BaseModel):
    def list_of_fields(self) -> List[str]:
        return list(self.model_fields.keys())


class HapiModelWithAdmins(BaseModel):
    location_ref: int = Field(description=truncate_query_description(DOC_LOCATION_REF))
    location_code: str = Field(max_length=128, description=truncate_query_description(DOC_LOCATION_CODE))
    location_name: str = Field(max_length=512, description=truncate_query_description(DOC_LOCATION_NAME))

    admin1_is_unspecified: bool = Field(exclude=True)
    admin2_is_unspecified: bool = Field(exclude=True)

    admin1_ref: int = Field(description=truncate_query_description(DOC_ADMIN1_REF))
    admin1_code: Optional[str] = Field(max_length=128, description=truncate_query_description(DOC_ADMIN1_CODE))
    admin1_name: Optional[str] = Field(max_length=512, description=truncate_query_description(DOC_ADMIN1_NAME))
    admin2_ref: int = Field(description=truncate_query_description(DOC_ADMIN2_REF))
    admin2_code: Optional[str] = Field(max_length=128, description=truncate_query_description(DOC_ADMIN2_CODE))
    admin2_name: Optional[str] = Field(max_length=512, description=truncate_query_description(DOC_ADMIN2_NAME))

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
