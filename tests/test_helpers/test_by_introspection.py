import pytest

from inspect import signature
from hdx_hapi.endpoints.get_idps import get_idps
from hdx_hapi.endpoints.get_affected_people import get_humanitarian_needs
from hdx_hapi.endpoints.get_operational_presence import get_operational_presences


GEOGRAPHIC_PARAMETERS = {
    'location_ref',
    'location_code',
    'location_name',
    'admin1_ref',
    'admin1_code',
    'admin1_name',
    'provider_admin1_name',
    'admin2_ref',
    'admin2_code',
    'admin2_name',
    'provider_admin2_name',
    'has_hrp',
    'in_gho',
}

ENDPOINT_FUNCTION_LIST = [get_idps, get_humanitarian_needs, get_operational_presences]


@pytest.mark.parametrize(
    'endpoint_function',
    ENDPOINT_FUNCTION_LIST,
)
def test_call_signatures_parametrically(endpoint_function):
    function_signature = signature(endpoint_function)

    query_parameters_set = {x for x, _ in function_signature.parameters.items()}

    assert GEOGRAPHIC_PARAMETERS.issubset(query_parameters_set)
