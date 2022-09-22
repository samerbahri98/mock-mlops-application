include .env
export

default:
	make up

.PHONY: kind-up
kind-up:
	sh ./scripts/kind_up.sh

.PHONY: kind-download
kind-download:
	sh ./scripts/download_kind.sh

.PHONY: kind-down
kind-down:
	sh ./scripts/kind_down.sh

.PHONY: up
up:
	make kind-download && make kind-up && docker compose up

.PHONY: down
down:
	make kind-down && docker compose down -v
