"""Users models."""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """User model."""

    email: str = models.EmailField(
        verbose_name=_("Email address"),
        unique=True
    )
    first_name: str = models.CharField(
        verbose_name=_("First name"),
        max_length=30,
        null=True
    )
    last_name: str = models.CharField(
        verbose_name=_("Last name"),
        max_length=150,
        null=True
    )
    phone: str = models.CharField(
        verbose_name=_("Phone number"),
        max_length=15,
        null=True
    )
    balance: float = models.DecimalField(max_digits=11, decimal_places=2, default=0)

    class Meta:
        """Meta."""

        ordering: list = ["-pk"]

    def __str__(self) -> str:
        """
        Call as string.

        :return: Self full name
        """
        return self.get_full_name()
