from hdx_hapi.endpoints.util.util import AdminLevel


def compute_unspecified_values(admin_level: AdminLevel):
    '''
    Compute unspecified values for admin1 and admin2
    '''
    admin1_is_unspecified = None
    admin2_is_unspecified = None
    if admin_level == AdminLevel.ZERO:
        admin1_is_unspecified = True
        admin2_is_unspecified = True
    elif admin_level == AdminLevel.ONE:
        admin1_is_unspecified = False
        admin2_is_unspecified = True
    elif admin_level == AdminLevel.TWO:
        admin1_is_unspecified = False
        admin2_is_unspecified = False
    return admin1_is_unspecified, admin2_is_unspecified