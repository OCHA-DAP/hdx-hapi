from pydantic import BaseModel, Field
from typing import Optional


class OperationalPresenceViewPydantic(BaseModel):
    id: int
    resource_ref: int
    org_ref: int
    # sector_code: str = Field(max_length=32)
    admin2_ref: int
    # reference_period_start: datetime
    # reference_period_end: Optional[datetime]
    source_data: Optional[str]

    class Config:
        orm_mode = True
