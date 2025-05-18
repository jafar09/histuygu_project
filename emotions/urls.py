from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Root URL ("/") now maps to index view
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("gallery_single/", views.gallery_single, name="gallery_single"),
    path("gallery/", views.gallery, name="gallery"),
    path("services/", views.services, name="services"),
    path("starter_page/", views.starter_page, name="starter_page"),
]
