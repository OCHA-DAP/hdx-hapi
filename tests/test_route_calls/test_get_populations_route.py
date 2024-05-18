import pytest
from hdx_hapi.endpoints.get_population import get_populations
from hdx_hapi.endpoints.util.util import (
    AdminLevel,
    CommonEndpointParams,
    OutputFormat,
    common_endpoint_parameters,
    PaginationParams,
)


@pytest.mark.asyncio
async def test_get_populations(event_loop, refresh_db, session_maker):
    db = session_maker()
    pagination_parameters = PaginationParams(limit=1000, offset=0)
    common_parameters = await common_endpoint_parameters(pagination_parameters=pagination_parameters)
    result = get_populations(
        common_parameters=common_parameters,
        db=db,
        gender_code=None,
        age_range_code=None,
        dataset_hdx_provider_stub=None,
        resource_update_date_min=None,
        resource_update_date_max=None,
        hapi_replaced_date_min=None,
        hapi_replaced_date_max=None,
        location_code=None,
        location_name=None,
        admin1_ref=None,
        admin1_name=None,
        location_ref=None,
        admin2_name=None,
        admin2_code=None,
        admin_level=AdminLevel.ONE,
        output_format=OutputFormat.JSON,
    )

    print(await result, flush=True)
    assert False
