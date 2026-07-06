.PHONY: run lint format test

run:
	python run.py

lint:
	python -m ruff check .

format:
	python -m black .

test:
	python -m pytest -q