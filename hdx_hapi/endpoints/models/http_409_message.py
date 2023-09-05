from pydantic import BaseModel


class HTTP409Message(BaseModel):
    detail: str
