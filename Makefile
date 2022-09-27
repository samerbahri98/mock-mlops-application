include .env
export

default: .up

.network-up:
	docker network ls | grep mock-mlops-network > /dev/null || docker network create mock-mlops-network

.network-down:
	docker network remove mock-mlops-network

.kind-up:
	sh ./scripts/kind_up.sh

.kind-download:
	sh ./scripts/download_kind.sh

.kind-down:
	sh ./scripts/kind_down.sh

.docker-up:
	docker compose up

.docker-prod-up:
	docker compose -f docker-compose.prod.yml up

.docker-prod-upd:
	docker compose -f docker-compose.prod.yml up -d

.docker-upd:
	docker compose up -d

.docker-down:
	docker compose down -v

.docker-prod-down:
	docker compose -f docker-compose.prod.yml down -v

.up: .network-up .kind-download .kind-up .docker-up

.prod-up: .network-up .kind-download .kind-up .docker-prod-up

.PHONY: up
up: .up

.PHONY: prod-up
prod-up: .prod-up

.PHONY: down
down: .kind-down .docker-down .network-down

.PHONY: prod-down
prod-down: .kind-down .docker-prod-down .network-down

.PHONY: network-up
network-up: .network-up

.PHONY: network-down
network-down: .network-down

.PHONY: restart
restart: down up

.PHONY: client
client:
	docker exec -it k8s-client sh