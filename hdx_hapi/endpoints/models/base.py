from typing import List
from pydantic import BaseModel


class HapiBaseModel(BaseModel):
    def list_of_fields(self) -> List[str]:
        return list(self.__fields__.keys())