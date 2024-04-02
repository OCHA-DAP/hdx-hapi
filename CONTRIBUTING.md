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

A local copy of HAPI can be run by importing a snapshot of the database from [here](https://github.com/OCHA-DAP/hapi-pipelines/tree/db-export/database). This is done using the following steps:

1. Running the `initialize_db.sh` script in the host.

2. Downloaded the database snapshot to the `docker/postgres-data/dbs/hapi-psql` folder in the host machine, this is mounted to `/var/lib/pgsql` folder in the `db` Docker container.

3. Importing the data is then done by running the following inside the `db` Docker container (*not* the application container):
    1. `cd /var/lib/pgsql`
    2. `pg_restore -U postgres --dbname hapi [dump filename].pg_restore`
    This import raises many error messages because the database already exists but the data appears to import successfully.

4. Setting the appropriate permissions by running `post_db_import.sh` from the host machine.

5. The docs and api can then be found at `http://localhost:8844/docs` in the host machine, once the application has been launched in the `hapi` container. This can be done using the Visual Code `start` launch target.

