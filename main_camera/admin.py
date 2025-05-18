from django.contrib import admin
from .models import EmotionImage
from django.utils.html import mark_safe

@admin.register(EmotionImage)
class EmotionImageAdmin(admin.ModelAdmin):
    list_display = ('emotion', 'created_at', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')
        return "Rasm yo'q"

    image_preview.short_description = 'Rasm'
