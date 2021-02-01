PIP_REQUIRED_VERSION=21.0.1

.PHONY: do-nothing
do-nothing:
	true

.PHONY: dev-env-setup
dev-env-setup:
	(test -n "${VIRTUAL_ENV}" && echo "Looks like virtualenv is activated (${VIRTUAL_ENV}). Deactivate it and try again.") || true
	test -z "${VIRTUAL_ENV}"
	pip install pip==${PIP_REQUIRED_VERSION}
	pip install virtualenvwrapper
	pip install poetry==1.1.4
	poetry config virtualenvs.path ${HOME}/.virtualenvs
	poetry run pip install pip==${PIP_REQUIRED_VERSION}
	poetry run pip install setuptools==53.0.0
