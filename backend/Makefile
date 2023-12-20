# Docker-related variables
DOCKER_COMPOSE = docker-compose
DOCKER_COMPOSE_FILE = docker-compose.yml

# Run the Django app using Docker
run:
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) run django-app

# Stop the Docker containers
stop:
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) down

# Run tests
test:
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) run pytest

