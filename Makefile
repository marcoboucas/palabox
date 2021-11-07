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


clean:
	rm -r test.* test2.* build dist ./**/palabox.egg-info


package:
	python setup.py sdist bdist_wheel

ship-test:
	python -m twine upload --repository testpypi dist/*

coverage:
	pytest --cov=palabox --cov-report=html tests/
	cd htmlcov && start "http://localhost:8000" && python -m http.server