#!/bin/sh

echo "Applying migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Creating superuser if not exists..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model

User = get_user_model()
if not User.objects.filter(username="123").exists():
    User.objects.create_superuser("123", "123@gmail.com", "123")
    print("Superuser created!")
else:
    print("Superuser already exists.")
EOF

echo "Starting Gunicorn..."
exec "$@"
