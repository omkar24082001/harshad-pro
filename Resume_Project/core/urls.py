from django.contrib import admin
from django.urls import path,include
from core import urls
from .views import home

urlpatterns = [
    path("", home, name="Home")
]