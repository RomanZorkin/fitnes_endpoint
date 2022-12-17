include .env
export

run:
	@python -m service


lint:
	@flake8 service
	@mypy service
