"""Pets models."""
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models.user import User


class Pet(models.Model):
    """Pet model."""

    breed: str = models.CharField(
        verbose_name=_("Breed of animal"),
        max_length=30,
    )
    nickname: str = models.CharField(
        verbose_name=_("Animal name"),
        max_length=30,
    )
    owner: User = models.ForeignKey(
        User,
        verbose_name=_("Owner"),
        on_delete=models.CASCADE,
        related_name="pets"
    )

    class Meta:
        """Meta."""

        ordering: list = ["-pk"]

    def __str__(self) -> str:
        """
        Call as string.

        :return: Pet info.
        """
        return f"Breed: {self.breed}. Nickname: {self.nickname}. Owner ID: {self.owner_id}"
