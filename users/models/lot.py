"""Lots models."""
from django.db import models
from django.utils.translation import gettext_lazy as _

from pets.models import Pet
from users import constants
from users.models.user import User


class Lot(models.Model):
    """Lot model."""

    pet: Pet = models.ForeignKey(
        Pet,
        verbose_name=_("Pet"),
        on_delete=models.SET_NULL,
        related_name="lots"
    )
    owner: User = models.ForeignKey(
        User,
        verbose_name=_("User"),
        on_delete=models.CASCADE,
        related_name="lots"
    )
    price: float = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    status: str = models.CharField(
        _('Статус'),
        choices=constants.STATUS_CHOICES,
        max_length=64,
        blank=False,
        null=False,
        default=constants.STATUS_NEW
    )

    class Meta:
        """Meta."""

        ordering: list = ["-pk"]

    def __str__(self) -> str:
        """
        Call as string.

        :return: Lot info
        """
        return f"Pet ID: {self.pet_id}. Price: {self.price}. Owner ID: {self.owner_id}"
