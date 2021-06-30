"""Auction URL Configuration."""

from django.contrib import admin
from django.urls import include, path

from auction.views import schema_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("docs/", schema_view.with_ui("redoc", cache_timeout=0),
         name="documentation"),
    path("", include("users.urls")),
    path("", include("authentication.urls")),
    path("", include("pets.urls")),
]
