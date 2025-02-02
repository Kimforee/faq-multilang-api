from rest_framework import generics
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer
from django.core.cache import cache
from django.shortcuts import render


class FAQListView(generics.ListAPIView):
    """API endpoint to fetch all FAQs with optional language translation."""

    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        """Override list method to handle caching of API responses."""
        lang = request.GET.get("lang", "en")
        cache_key = f"faqs_list_{lang}"
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        # Cache response for 1 hour
        cache.set(cache_key, serializer.data, timeout=3600)
        return Response(serializer.data)

def faq_list_view(request):
    """Renders a simple template to display FAQs with language selection."""
    lang = request.GET.get("lang", "en")
    faqs = [faq.get_translated_faq(lang) for faq in FAQ.objects.all()]
    
    return render(request, "faqs/faq_list.html", {"faqs": faqs})