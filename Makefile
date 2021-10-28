lint:
	python -m pylint palabox
	python -m mypy palabox
	python -m flake8 palabox

test:
	pytest


install:
	pip install -r requirements.txt
install-dev: install
	pip install -r requirements-dev.txt