from django.urls import path
from .views import FAQListView, faq_list_view

urlpatterns = [
    path("", FAQListView.as_view(), name="faq-list"),
]
