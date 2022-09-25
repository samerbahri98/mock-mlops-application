include .env
export

default: .up

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



.up: .kind-download .kind-up .docker-up

.PHONY: up
up: .up

.PHONY: down
down: .kind-down .docker-down

.PHONY: client
client:
	docker exec -it k8s-client sh