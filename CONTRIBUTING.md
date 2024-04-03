# Contributing 

The Humanitarian API (HAPI) is being developed by a team from the [Centre for Humanitarian Data](https://centre.humdata.org/).

HDX developers are using [Visual Code](https://code.visualstudio.com/) as a standard IDE for this project with development taking place inside Docker containers.

The following needs to be run once to setup the Docker containers for testing:

```shell
cd docker
docker-compose up -d
docker-compose exec -T hapi sh -c "apk add git"
docker-compose exec -T hapi sh -c "pip install --upgrade -r requirements.txt"
docker-compose exec -T hapi sh -c "pip install --upgrade -r dev-requirements.txt"
cd ..
./initialize_test_db.sh
```

Tests can either be run from the Visual Code test runner or with:

```shell
docker-compose exec -T hapi sh -c "pytest --log-level=INFO --cov=. --cov-report term --cov-report xml:coverage.xml"
```

A local copy of HAPI can be run by importing a snapshot of the database using the following shell script invocation in the host machine.

```shell
 ./restore_database.sh https://github.com/OCHA-DAP/hapi-pipelines/raw/db-export/database/hapi_db.pg_restore hapi
```

The HAPI application can then be launched using the `start` launch configuration in Visual Code, this serves the documentation at `http://localhost:8844/docs` and the API at `http://localhost:8844/api` in the host machine.

The HAPI database can be accessed locally with the following connection details: 

```
URL: jdbc:postgresql://localhost:45432/hapi
username: hapi
password: hapi
```