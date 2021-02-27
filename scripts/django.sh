#!/bin/sh

poetry run python manage.py makemigrations
poetry run python manage.py migrate

poetry run python manage.py setuptestdb

poetry run gunicorn stts.wsgi -b 0.0.0.0:8000
