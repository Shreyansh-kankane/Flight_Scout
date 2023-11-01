from django.contrib import admin
from django.urls import path
from .views import flight_reservation


urlpatterns = [
    path("", flight_reservation, name="index"),
]
