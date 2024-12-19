APP_NAME := dobby


all: docker run log

docker:
	@echo '\n'------------- [building docker images] -------------
	@DOCKER_DEFAULT_PLATFORM=linux/amd64 docker compose build

run:
	@echo '\n'------------- [run docker containers] -------------  
	@APP_NAME=${APP_NAME} docker compose up 
restart:
	@docker compose restart

down:
	@docker compose down

log:
	@docker compose logs -f app
run-tests:
	@echo '\n'------------- [run tests] -------------
	@docker compose exec fastapi_service python3 -m pytest
create-kafka-topic:
	@echo '\n'------------- [create kafka topic] -------------
	@docker compose exec kafka kafka-topics.sh --create --bootstrap-server localhost:9092 --topic texts_topic --partitions 1 --replication-factor 1 --if-not-exists