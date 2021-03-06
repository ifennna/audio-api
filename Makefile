.PHONY: run migrate test db stop-db

db:
	docker-compose up -d

stop-db:
	docker-compose down

migrate:
	python start.py db upgrade

run:
	python start.py run

test:
	python start.py test