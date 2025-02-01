import pytest
from rest_framework.test import APIClient
from faqs.models import FAQ


@pytest.mark.django_db
def test_get_faqs():
    client = APIClient()
    FAQ.objects.create(question="What is Django?", answer="Django is a framework.")

    response = client.get("/api/faqs/")
    assert response.status_code == 200
    assert len(response.json()) > 0


@pytest.mark.django_db
def test_get_faqs_with_translation():
    client = APIClient()
    faq = FAQ.objects.create(
        question="What is Django?", answer="Django is a framework."
    )

    response = client.get("/api/faqs/?lang=hi")
    assert response.status_code == 200
    assert "Django" in response.json()[0]["question"]
