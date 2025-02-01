import pytest
from faqs.models import FAQ


@pytest.mark.django_db
def test_faq_model():
    faq = FAQ.objects.create(
        question="What is Django?", answer="Django is a web framework."
    )

    assert faq.question == "What is Django?"
    assert faq.answer == "Django is a web framework."


@pytest.mark.django_db
def test_faq_translation():
    faq = FAQ.objects.create(
        question="What is Django?", answer="Django is a web framework."
    )

    translated = faq.get_translated_faq("hi")
    assert "Django" in translated["question"]  # Hindi translation should contain Django
