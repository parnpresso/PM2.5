#!/usr/bin/env bash

sleep 10

cd /app/pm25
celery -A pm25 beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
