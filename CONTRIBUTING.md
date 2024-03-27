# Contributing 

The Humanitarian API (HAPI) is being developed by a team from the [Centre for Humanitarian Data](https://centre.humdata.org/).

Developers are using [Visual Code](https://code.visualstudio.com/) as a standard IDE for this project with development taking place in `devcontainers`, thus [Docker Desktop](https://www.docker.com/products/docker-desktop/) is also required.

The following need to be run once to setup the Docker containers for testing:

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

A local copy of HAPI can be run by importing a snapshot of the database from [here](https://github.com/OCHA-DAP/hapi-pipelines/tree/db-export/database).

** Import instructions to follow
** Launch/browse instructions to follow