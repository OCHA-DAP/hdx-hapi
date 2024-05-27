from pydantic import Field


PERCENTAGE_TYPE = Field(ge=0, le=100)
