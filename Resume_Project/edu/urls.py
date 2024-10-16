from django.contrib import admin
from django.urls import path, include
from .views import contact,submit_form

urlpatterns = [
    path("contact/",contact,name = "contact"),
    path("contact/submit-form/",submit_form,name = "email")
]