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

echo "Inserting default FAQs..."
python manage.py shell <<EOF
from faqs.models import FAQ

if not FAQ.objects.filter(question="What is Django?").exists():
    faq1 = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a high-level Python web framework."
    )
    print(faq1.get_translated_faq("hi"))  # Fetch Hindi translation
    print(faq1.get_translated_faq("bn"))  # Fetch Bengali translation

if not FAQ.objects.filter(question="How does Django handle requests?").exists():
    faq2 = FAQ.objects.create(
        question="How does Django handle requests?",
        answer="Django follows the MVT (Model-View-Template) architecture."
    )
    print(faq2.get_translated_faq("hi"))  # Fetch Hindi translation
    print(faq2.get_translated_faq("bn"))  # Fetch Bengali translation
EOF

echo "Starting Gunicorn..."
exec "$@"
