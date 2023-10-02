project=endpoints
venv=env
python=$(venv)/bin/python
linter=$(venv)/bin/flake8
pypi_mode=test
pypi_package_name=$(shell $(python) -c "from $(project) import __app_name__; print(__app_name__)")

project_version=$(shell $(python) -c "from $(project) import __version__; print(__version__)")
git_version=$(shell git describe --tags)

ifeq ($(pypi_mode),test)
	pypi_url=pypi_test
endif
ifeq ($(pypi_mode),production)
	pypi_url=pypi
endif


test:
	$(python) -m unittest

lint:
	$(linter) endpoints/
	$(linter) tests.py

build_pypi: lint test
	$(python) setup.py bdist_wheel

check_semver:
ifneq ($(git_version),$(project_version))
	@echo "[$(git_version)] != [$(project_version)]"
	exit 1
endif

publish_pypi: lint test check_semver build_pypi
	twine upload \
		-r $(pypi_url) \
		dist/$(pypi_package_name)-$(project_version)-py3-none-any.whl
