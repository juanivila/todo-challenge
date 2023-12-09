#!/usr/bin/env sh

echo "Apply database migrations"
python manage.py migrate
chmod +w /usr/src/app/db.sqlite3


echo "Create Django superuser"
DJANGO_SUPERUSER_PASSWORD="admin" python manage.py createsuperuser --noinput \
    --username=admin \
    --email=admin@example.com

exec "$@"
