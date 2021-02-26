#!/bin/bash

poetry run celery -A stts worker -l info
