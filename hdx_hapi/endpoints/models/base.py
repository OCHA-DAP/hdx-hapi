from typing import Generic, List, Optional, TypeVar
from pydantic import BaseModel, ConfigDict


class HapiBaseModel(BaseModel):
    def list_of_fields(self) -> List[str]:
        return list(self.model_fields.keys())


DataT = TypeVar('DataT')


class HapiGenericResponse(BaseModel, Generic[DataT]):
    data: List[DataT]

    model_config = ConfigDict(from_attributes=True)
