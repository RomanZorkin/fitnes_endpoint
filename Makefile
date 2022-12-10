include .env
export

run:
	@python -m service


lint:
	@mypy service
	@flake8 service

