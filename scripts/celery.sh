#!/bin/sh

poetry run celery -A stts worker -l info
