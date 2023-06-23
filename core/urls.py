from django.urls import path
from . import views

urlpatterna = [
    path("", views.index, name="index"),
]
