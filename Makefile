install:
	uv install

run-local:
	uv run alembic upgrade head
	uv run uvicorn src.app.main:app --host 0.0.0.0 --port 8000 --reload --reload-dir . --log-config=log_config.ini --log-level=debug

build:
	uv run docker-compose -f docker-compose.$(for).yml build

start:
	uv run docker-compose -f docker-compose.$(for).yml up --force-recreate --remove-orphans

up:
	uv run docker-compose -f docker-compose.$(for).yml up --force-recreate --remove-orphans -d

stop:
	uv run docker-compose -f docker-compose.$(for).yml stop

rm:
	uv run docker-compose -f docker-compose.$(for).yml rm
	sudo rm -rf db

revision:
	uv run docker run app /bin/bash -c "uv run alembic revision --autogenerate"

upgrade:
	uv run docker run app /bin/bash -c "uv run alembic upgrade $(revision)"

downgrade:
	uv run docker run app /bin/bash -c "uv run alembic downgrade $(revision)"

test:
	uv run docker-compose -f docker-compose.test.yml up --force-recreate --remove-orphans --abort-on-container-exit

test-local:
	uv run alembic upgrade head
	uv run pytest -s --verbose

lint:
	uv run flake8
	uv run mypy -p src --cache-dir=/dev/null --config-file=pyproject.toml
	uv run mypy -p tests --cache-dir=/dev/null --config-file=pyproject.toml
	uv run mypy -p migrations --cache-dir=/dev/null --config-file=pyproject.toml
