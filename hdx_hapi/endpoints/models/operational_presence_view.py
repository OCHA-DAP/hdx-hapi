from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class OperationalPresenceViewPydantic(BaseModel):

    sector_code: str = Field(max_length=32)
    dataset_hdx_stub: str = Field(max_length=128)
    resource_hdx_id: str = Field(max_length=36)
    org_acronym: str = Field(max_length=32)
    org_name: str = Field(max_length=512)
    sector_name: str = Field(max_length=512)
    location_code: str = Field(max_length=128)
    location_name: str = Field(max_length=512)
    admin1_code: str = Field(max_length=128)
    admin1_name: str = Field(max_length=512)
    admin2_code: str = Field(max_length=128)
    admin2_name: str = Field(max_length=512)
    # TODO remove this field after testing and validation. might be helpful to have it displayed
    resource_update_date: datetime
    # org_ref: int = None,
    # dataset_hdx_id: str = Field(max_length=36),
    # dataset_title: str = Field(max_length=1024),
    # dataset_provider_code: str = Field(max_length=128),
    # dataset_provider_name: str = Field(max_length=512),
    # resource_filename: str = Field(max_length=256),
    # org_type_code: str = Field(max_length=32),
    # org_type_description: str = Field(max_length=512),


    class Config:
        orm_mode = True
