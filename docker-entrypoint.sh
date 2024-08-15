#!/bin/sh

python manage.py migrate
python manage.py collectstatic --no-input
gunicorn --bind 0.0.0.0:8000 --worker-class gthread --threads 4 core.wsgi:application