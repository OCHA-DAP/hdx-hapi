from typing import Tuple, Optional
from fastapi import HTTPException, status

from hdx_hapi.endpoints.util.util import AdminLevel


def compute_unspecified_values(admin_level: Optional[AdminLevel], provider_admin1_name: Optional[str], 
                               provider_admin2_name: Optional[str]) -> Tuple[Optional[bool], Optional[bool], 
                                                                             Optional[bool], Optional[bool]]:
    """
    Compute unspecified values for admin1 and admin2
    """
    admin1_is_unspecified = None
    admin2_is_unspecified = None
    provider_admin1_name_unspecified = None
    provider_admin2_name_unspecified = None
    if admin_level == AdminLevel.ZERO:
        admin1_is_unspecified = True
        admin2_is_unspecified = True
        provider_admin1_name_unspecified = True
        provider_admin2_name_unspecified = True
    elif admin_level == AdminLevel.ONE:
        admin1_is_unspecified = False
        admin2_is_unspecified = True
        provider_admin1_name_unspecified = False
        provider_admin2_name_unspecified = True
    elif admin_level == AdminLevel.TWO:
        admin1_is_unspecified = False
        admin2_is_unspecified = False
        provider_admin1_name_unspecified = False
        provider_admin2_name_unspecified = False
    if admin1_is_unspecified and provider_admin1_name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail='Cannot specify provider_admin1_name and admin level filter'
        )
    if admin2_is_unspecified and provider_admin2_name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail='Cannot specify provider_admin2_name and admin level filter'
        )
    return admin1_is_unspecified, admin2_is_unspecified, \
            provider_admin1_name_unspecified, provider_admin2_name_unspecified
