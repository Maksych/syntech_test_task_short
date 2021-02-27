FROM python:3.9

WORKDIR /home/app

RUN python -m pip install -U pip setuptools \
    && pip install poetry

COPY pyproject.toml .

RUN poetry install

COPY ./src .
COPY .env .
COPY ./scripts .

RUN chmod +x django.sh celery.sh
