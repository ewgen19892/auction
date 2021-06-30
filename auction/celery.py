"""Celery app."""
import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auction.settings")

app: Celery = Celery("Auction")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
