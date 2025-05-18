from django.urls import path
from .views import detect_emotion_view

urlpatterns = [
    path('', detect_emotion_view, name='detect'),
]