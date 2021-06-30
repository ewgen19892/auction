"""Bets models."""
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models.lot import Lot
from users.models.user import User


class Bet(models.Model):
    """Bet model."""

    user: User = models.ForeignKey(
        User,
        verbose_name=_("User"),
        on_delete=models.CASCADE,
        related_name="user_bets"
    )
    lot: Lot = models.ForeignKey(
        Lot,
        verbose_name=_("Lot"),
        on_delete=models.CASCADE,
        related_name="bets"
    )
    amount: float = models.DecimalField(max_digits=11, decimal_places=2, default=0)

    class Meta:
        """Meta."""

        ordering: list = ["-pk"]

    def __str__(self) -> str:
        """
        Call as string.

        :return: User ID and amount
        """
        return f"User ID: {self.user_id}. Amount: {self.amount}"
