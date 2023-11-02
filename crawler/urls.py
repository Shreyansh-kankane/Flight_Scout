from django.contrib import admin
from django.urls import path
from .views import flight_reservation, inputs


urlpatterns = [
    path("", flight_reservation, name="index"),
    path("inputs/", inputs)
]
