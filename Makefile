install:
		poetry install

build:
		poetry build

reinstall:
		pip install --user --force-reinstall dist/*.whl

dev:
		poetry run python manage.py runserver

start:
		poetry run gunicorn test_task_rishat.wsgi

migrate:
		poetry run python manage.py migrate