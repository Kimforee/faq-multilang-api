from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from googletrans import Translator


class FAQ(models.Model):
    LANGUAGE_CHOICES = [
        ("en", "English"),
        ("hi", "Hindi"),
        ("bn", "Bengali"),
    ]

    question = models.TextField()
    answer = RichTextField()  # WYSIWYG Editor support

    # Translations
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def translate_text(self, text, dest_lang):
        """Helper function to translate text dynamically."""
        if not text:
            return ""
        translator = Translator()
        return translator.translate(text, dest=dest_lang).text

    def get_translated_faq(self, lang="en"):
        """Retrieve translated question & answer with Redis caching."""
        cache_key = f"faq_{self.id}_{lang}"
        cached_data = cache.get(cache_key)

        if cached_data:
            return cached_data  # Return cached translation

        # Perform translation if not cached
        translated_data = self._translate_faq(lang)

        # Store translation in cache
        cache.set(cache_key, translated_data, timeout=3600)
        return translated_data

    def _translate_faq(self, lang):
        """Translate FAQ dynamically if translation fields are empty."""
        translator = Translator()
        if lang == "hi":
            return {
                "question": self.question_hi
                or translator.translate(self.question, dest="hi").text,
                "answer": self.answer_hi
                or translator.translate(self.answer, dest="hi").text,
            }
        elif lang == "bn":
            return {
                "question": self.question_bn
                or translator.translate(self.question, dest="bn").text,
                "answer": self.answer_bn
                or translator.translate(self.answer, dest="bn").text,
            }
        return {"question": self.question, "answer": self.answer}

    def save(self, *args, **kwargs):
        """Auto-translate when saving an FAQ."""
        if not self.question_hi:
            self.question_hi = self.translate_text(self.question, "hi")
        if not self.question_bn:
            self.question_bn = self.translate_text(self.question, "bn")
        if not self.answer_hi:
            self.answer_hi = self.translate_text(self.answer, "hi")
        if not self.answer_bn:
            self.answer_bn = self.translate_text(self.answer, "bn")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.question[:50] + "..."  # Display first 50 chars
