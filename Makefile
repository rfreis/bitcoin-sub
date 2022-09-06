build:
	docker-compose build bitcoin_sub

local-bash:
	docker-compose exec bitcoin_sub /bin/bash

logs:
	docker-compose logs --follow --tail=20 bitcoin_sub

unit:
	docker-compose exec bitcoin_sub coverage run -m pytest tests/unit -v -x
	docker-compose exec bitcoin_sub coverage xml --ignore-errors
	@echo "Total Python coverage:" `docker-compose exec bitcoin_sub coverage report --precision=2 | tail -n 1 | awk '{ print $4 }'`

test:
	docker-compose exec bitcoin_sub coverage run -m pytest tests/ -v -x
	docker-compose exec bitcoin_sub coverage xml --ignore-errors
	@echo "Total Python coverage:" `docker-compose exec bitcoin_sub coverage report --precision=2 | tail -n 1 | awk '{ print $4 }'`

pre-commit-install:
	docker-compose exec bitcoin_sub pre-commit install

start-local:
	docker-compose up -d

stop:
	docker-compose down
