from typing import Generic, List, Optional, TypeVar
from typing_extensions import Self
from pydantic import BaseModel, ConfigDict, Field, model_validator

from hdx_hapi.config.doc_snippets import (
    DOC_LOCATION_CODE,
    # DOC_LOCATION_REF,
    DOC_LOCATION_NAME,
    # DOC_ADMIN1_REF,
    DOC_ADMIN1_NAME,
    DOC_ADMIN1_CODE,
    # DOC_PROVIDER_ADMIN1_NAME,
    # DOC_ADMIN2_REF,
    DOC_ADMIN2_NAME,
    DOC_ADMIN2_CODE,
    # DOC_PROVIDER_ADMIN2_NAME,
    DOC_ADMIN_LEVEL_FILTER,
    truncate_query_description,
)
from hdx_hapi.endpoints.models.util.constants import AdminLevelInt


class HapiBaseModel(BaseModel):
    def list_of_fields(self) -> List[str]:
        return list(self.model_fields.keys())


class HapiModelWithAdmin1(BaseModel):
    location_code: str = Field(max_length=128, description=truncate_query_description(DOC_LOCATION_CODE))
    location_name: str = Field(max_length=512, description=truncate_query_description(DOC_LOCATION_NAME))

    admin1_code: Optional[str] = Field(max_length=128, description=truncate_query_description(DOC_ADMIN1_CODE))
    admin1_name: Optional[str] = Field(max_length=512, description=truncate_query_description(DOC_ADMIN1_NAME))

    provider_admin1_name: Optional[str] = Field(exclude=True, max_length=512)

    admin_level: int = Field(description=truncate_query_description(DOC_ADMIN_LEVEL_FILTER))

    @model_validator(mode='after')  # type: ignore
    def set_admin1_name(self) -> Self:
        # If 'admin1_name' is None, set 'admin1_name' is set to _provider_admin1_name
        if (not self.admin1_name or self.admin1_name.lower() == 'unspecified') and self.provider_admin1_name:
            self.admin1_name = self.provider_admin1_name

        return self

    @model_validator(mode='after')  # type: ignore
    def set_admin1_admin2_null(self) -> Self:
        if self.admin_level is not None:
            if self.admin_level == AdminLevelInt.ZERO:
                self.admin1_code = None
                self.admin1_name = None
        return self


class HapiModelWithAdmins(BaseModel):
    location_code: str = Field(max_length=128, description=truncate_query_description(DOC_LOCATION_CODE))
    location_name: str = Field(max_length=512, description=truncate_query_description(DOC_LOCATION_NAME))
    admin1_code: Optional[str] = Field(max_length=128, description=truncate_query_description(DOC_ADMIN1_CODE))
    admin1_name: Optional[str] = Field(max_length=512, description=truncate_query_description(DOC_ADMIN1_NAME))
    admin2_code: Optional[str] = Field(max_length=128, description=truncate_query_description(DOC_ADMIN2_CODE))
    admin2_name: Optional[str] = Field(max_length=512, description=truncate_query_description(DOC_ADMIN2_NAME))

    provider_admin1_name: Optional[str] = Field(exclude=True, default=None, max_length=512)
    provider_admin2_name: Optional[str] = Field(exclude=True, default=None, max_length=512)

    admin_level: int = Field(description=truncate_query_description(DOC_ADMIN_LEVEL_FILTER))

    @model_validator(mode='after')  # type: ignore
    def set_admin1_admin2_name(self) -> Self:
        # If 'admin1_name' is None, set 'admin1_name' is set to _provider_admin1_name
        if (not self.admin1_name or self.admin1_name.lower() == 'unspecified') and self.provider_admin1_name:
            self.admin1_name = self.provider_admin1_name

        # If 'admin2_name' is None, set 'admin2_name' is set to _provider_admin2_name
        if (not self.admin2_name or self.admin2_name.lower() == 'unspecified') and self.provider_admin2_name:
            self.admin2_name = self.provider_admin2_name

        return self

    @model_validator(mode='after')  # type: ignore
    def set_admin1_admin2_null(self) -> Self:
        if self.admin_level is not None:
            if self.admin_level == AdminLevelInt.ZERO:
                self.admin1_code = None
                self.admin1_name = None
                self.admin2_code = None
                self.admin2_name = None
            if self.admin_level == AdminLevelInt.ONE:
                self.admin2_code = None
                self.admin2_name = None
        return self


DataT = TypeVar('DataT')


class HapiGenericResponse(BaseModel, Generic[DataT]):
    data: List[DataT]

    model_config = ConfigDict(from_attributes=True)
