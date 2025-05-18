from django.urls import path
from . import views

urlpatterns = [
    path('camera/', views.camera_view, name='camera_view'),
    path('upload_image/', views.upload_image, name='upload_image'),
]
