include .env
export

default: .up

.network-up:
	docker network create mock-mlops-network

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

.docker-upd:
	docker compose up -d

.docker-down:
	docker compose down -v



.up: .network-up .kind-download .kind-up .docker-up

.PHONY: up
up: .up

.PHONY: down
down: .kind-down .docker-down .network-down

.PHONY: network-up
network-up: .network-up

.PHONY: network-down
network-down: .network-down

.PHONY: client
client:
	docker exec -it k8s-client sh