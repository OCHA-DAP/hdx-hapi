import pytest
from hdx_hapi.endpoints.get_population import get_populations
from hdx_hapi.endpoints.util.util import (
    PaginationParams,
    OutputFormat,
    common_endpoint_parameters,
    reference_period_parameters,
    AdminLevel,
)


@pytest.mark.asyncio
async def test_get_populations(event_loop, refresh_db, session_maker):
    db = session_maker()
    pagination_parameters = PaginationParams(limit=1000, offset=0)
    common_parameters = await common_endpoint_parameters(pagination_parameters=pagination_parameters)
    results = get_populations(
        common_parameters=common_parameters,
        ref_period_parameters=reference_period_parameters,
        db=db,
        admin2_ref=None,
        gender=None,
        age_range=None,
        min_age=None,
        max_age=None,
        population=None,
        location_ref=None,
        location_code=None,
        location_name=None,
        admin1_ref=None,
        admin1_code=None,
        admin1_name=None,
        admin2_name=None,
        admin2_code=None,
        admin_level=AdminLevel.ONE,
        output_format=OutputFormat.JSON,
    )

    print(results, flush=True)
    assert True
