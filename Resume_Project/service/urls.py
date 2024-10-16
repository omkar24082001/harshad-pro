from django.contrib import admin
from django.urls import path,include
from .views import service


urlpatterns = [
    path("service/",service,name = "service")
]