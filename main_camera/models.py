from django.db import models

# Create your models here.

class EmotionImage(models.Model):
    image = models.ImageField(upload_to='images/')
    emotion = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.emotion} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"

