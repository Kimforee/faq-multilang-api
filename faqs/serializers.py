from rest_framework import serializers
from .models import FAQ


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ["id", "question", "answer", "created_at"]

    def to_representation(self, instance):
        """Modify response to include translated content dynamically."""
        lang = self.context.get("request").GET.get("lang", "en")
        translated_faq = instance.get_translated_faq(lang)

        data = super().to_representation(instance)
        data["question"] = translated_faq["question"]
        data["answer"] = translated_faq["answer"]
        return data
