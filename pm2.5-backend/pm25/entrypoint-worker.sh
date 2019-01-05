#!/usr/bin/env bash

cd /app/pm25
celery -A pm25 worker -l info -n events_worker
