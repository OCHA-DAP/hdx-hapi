cd docker
docker-compose exec -T hapi sh -c "pip install -r dev-requirements.txt"
docker-compose exec hapi sh -c "mkdocs serve --dev-addr 0.0.0.0:5001"
cd ..