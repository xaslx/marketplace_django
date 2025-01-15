DC = docker compose
STORAGES_FILE = docker_compose/storages.yaml
EXEC = docker exec -it
DB_CONTAINER = postgresdb
LOGS = docker logs
ENV = --env-file .env
APP_FILE = docker_compose/app.yaml
APP_CONTAINER = main-app


.PHONY: storages
storages:
	${DC} -f ${STORAGES_FILE} ${ENV} up -d

.PHONY: storages-down
storages-down:
	${DC} -f $(STORAGES_FILE) down


.PHONY: postgres
postgres:
	${EXEC} ${DB_CONTAINER} psql -U postgres

.PHONY: storages-logs
storages-logs:
	${LOGS} ${DB_CONTAINER} -f


.PHONY: app
app:
	${DC} -f ${APP_FILE} -f ${STORAGES_FILE} ${ENV} up -d


.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER} -f


.PHONY: app-down
app-down:
	${DC} -f $(STORAGES_FILE) -f ${APP_FILE} down