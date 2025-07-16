clean:
	poetry env remove --all
	rm -rf dist/*

lock:
	poetry lock

install: lock
	poetry install --all-extras --all-groups

test: install
	poetry run python -m unittest discover -s tests -t src

lint:
	poetry run isort src/
	poetry run black src/
	poetry run ruff check src/

shell:
	poetry run python

build:
	poetry build

publish:
	poetry publish
