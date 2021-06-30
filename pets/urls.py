"""Pets URL Configuration."""
from django.urls import path

from pets.views import PetDetail, PetList

app_name = "pets"
urlpatterns = [

    path("pets/", PetList.as_view(), name="pet_list"),
    path("pets/<slug:pk>/", PetDetail.as_view(), name="pet_detail"),

]
