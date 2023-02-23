from . import views
from django.urls import path

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("gallery", views.gallery, name="gallery")
]