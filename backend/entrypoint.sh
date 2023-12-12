#!/usr/bin/env sh

echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate
chmod +w /usr/src/app/db.sqlite3
mkdir logs
chmod +w /usr/src/app/logs


echo "Create Django superuser"
DJANGO_SUPERUSER_PASSWORD="admin" python manage.py createsuperuser --noinput \
    --username=admin \
    --email=admin@example.com


echo "Create Django superuser 2"
DJANGO_SUPERUSER_PASSWORD="admin" python manage.py createsuperuser --noinput \
    --username=admin2 \
    --email=admin2@example.com

exec "$@"
