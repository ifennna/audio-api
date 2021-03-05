.PHONY: run migrate test

migrate:
	python start.py db upgrade

run:
	python start.py run

test:
	python start.py test