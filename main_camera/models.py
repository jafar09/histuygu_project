from django.db import models

# Create your models here.

class EmotionImage(models.Model):
    image = models.ImageField(upload_to='images/')
    emotion = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.emotion} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"

    def image_tag(self):
        if self.image:
            return f'<img src="{self.image.url}" width="150" />'
        return "Rasm yo'q"

    image_tag.short_description = 'Rasm'
    image_tag.allow_tags = True
