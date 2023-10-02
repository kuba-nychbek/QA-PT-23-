from django.contrib import admin
from django.urls import path
from Kylym.views import name_representative

urlpatterns = [
    path('', name_representative, name="start_project"),
]
