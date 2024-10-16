from django.contrib import admin
from django.urls import path, include
from .views import skill

urlpatterns = [
    path("skill/",skill,name = "skill")
]