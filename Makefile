.PHONY: run migrate

migrate:
	python start.py db upgrade

run:
	python start.py run