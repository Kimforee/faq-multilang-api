from django.contrib import admin
from .models import FAQ


class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "created_at")
    search_fields = ("question", "question_hi", "question_bn")


admin.site.register(FAQ, FAQAdmin)
