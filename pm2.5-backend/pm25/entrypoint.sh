#!/usr/bin/env bash

sleep 5

python3 pm25/manage.py migrate

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('parn', 'parn@parn.co', 'parn1234')" | python3 pm25/manage.py shell

python3 pm25/manage.py runserver 0.0.0.0:8000
