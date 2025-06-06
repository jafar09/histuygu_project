from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"