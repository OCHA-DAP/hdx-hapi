# Contributing 

The Humanitarian API (HDX HAPI) is being developed by a team from the [Centre for Humanitarian Data](https://centre.humdata.org/).

HDX developers are using [Visual Code](https://code.visualstudio.com/) as a standard IDE for this project with development taking place inside Docker containers.

The following needs to be run once to setup the Docker containers for testing:

```shell
cd docker
docker-compose up -d
docker-compose exec -T hapi sh -c "apk add git"
docker-compose exec -T hapi sh -c "pip install --upgrade -r requirements.txt"
docker-compose exec -T hapi sh -c "pip install --upgrade -r dev-requirements.txt"
```
This makes an editable installation of `hapi-sqlalchemy-schema` inside this repository.

Then for each session the following needs to be run:
```shell
cd docker
docker-compose up -d
cd ..
./initialize_test_db.sh
./restore_database.sh https://github.com/OCHA-DAP/hapi-pipelines/raw/db-export/database/hapi_db.pg_restore hapi
```



Tests can either be run from the Visual Code test runner or with:

```shell
docker-compose exec -T hapi sh -c "pytest --log-level=INFO --cov=. --cov-report term --cov-report xml:coverage.xml"
```

As an integration test the `docs` endpoint is inspected "manually".

A local copy of HDX HAPI can be run by importing a snapshot of the database using the following shell script invocation in the host machine.

```shell
 ./restore_database.sh https://github.com/OCHA-DAP/hapi-pipelines/raw/db-export/database/hapi_db.pg_restore hapi
```

The HDX HAPI application can then be launched using the `start` launch configuration in Visual Code, this serves the documentation at `http://localhost:8844/docs` and the API at `http://localhost:8844/api` in the host machine.

The HDX HAPI database can be accessed locally with the following connection details: 

```
URL: jdbc:postgresql://localhost:45432/hapi
username: hapi
password: hapi
```

# Adding a new endpoint

To add a new endpoint we add lines like this to `main.py`:
```python
from hdx_hapi.endpoints.get_population_profile import router as population_profile_router  # noqa
```

Followed by:
```python
app.include_router(population_profile_router)
```

The route is implemented in the `hdx_hapi/endpoints` directory based on a FastAPI `APIRouter`. `pagingination_parameters` and `OutputFormat` are provided as parameters for all endpoints. The model for the response is provided in the `hdx_hapi/endpoints/models` directory, derived from the HapiBaseModel which is itself derived from the `pydantic.BaseModel`

Tests are created by adding dictionary entries with `query_parameters` and `expected_fields` to the `tests/endpoint_data.py` file. Three tests are then done in a dedicated test file, one for any response, one for the query parameters and one for the response.

# Add a new parameter to an existing endpoint

To add a new query parameter to an endpoint, and to the response the general strategy is as follows. This description is based on [this](https://github.com/OCHA-DAP/hdx-hapi/pull/184) PR:

1. Add lines like this to the relevant View class in`hdx_hapi/db/models/views/all_views.py`:
```python
has_hrp: Mapped[bool] = column_property(location_view.c.has_hrp)
in_gho: Mapped[bool] = column_property(location_view.c.in_gho)
```
1. Add lines like this to the router for the endpoint in one of the files in `hdx_hapi/endpoints`:
```python
has_hrp: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_HAS_HRP}')] = None,
in_gho: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_IN_GHO}')] = None,
```
The new parameters need to be added into the call to the subsequent `get_*_srv` call:
```python
has_hrp=has_hrp,
in_gho=in_gho,
```
1. The `get_*_srv` function in `hdx_hapi/services/get_*_srv.py` needs to be updated with the new query parameters:
```python
has_hrp: Optional[bool] = None,
in_gho: Optional[bool] = None,
```
Again the new parameters need to be included in the subsequent call to the next function `*_view_list`:
```python
has_hrp: Optional[bool] = None,
in_gho: Optional[bool] = None,
```
It is the `*_view_list` function in files like `hdx_hapi/db/dao/*_view_dao.py` where queries happen. The new query parameters need to be added to the function signature:
```python
has_hrp: Optional[bool] = None,
in_gho: Optional[bool] = None,
```
And the relevant query added, for these boolean parameters it is easy:
```python
if has_hrp:
    query = query.where(LocationView.has_hrp == has_hrp)
if in_gho:
    query = query.where(LocationView.in_gho == in_gho)
```
Actually in this case we do not need to make this explicit conditional statements because the parameters we introduce here are in the `EntityWithLocationAdmin` class and are handled by `apply_location_admin_filter`.
1. If required, the response model class in files in `hdx_hapi/endpoints/models/` needs updating:
```python
has_hrp: bool = Field(description=truncate_query_description(DOC_LOCATION_HAS_HRP))
in_gho: bool =Field(description=truncate_query_description(DOC_LOCATION_IN_GHO))
```
Again, because this is a special case where the parameters are in the `HapiModelWithAdmins` class it is not required for these particular parameters.
1. Finally test fixtures need to be updated in `tests/test_endpoints/endpoint_data.py`, `tests/sample_data/*.sql` and sometimes in the declaration of `Response` classes in the tests themselves.