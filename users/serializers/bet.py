"""Bets serializers."""
from rest_framework import serializers

from users.models.bet import Bet
from users.serializers import UserSerializer
from users.serializers.lot import LotSerializer


class BetSerializer(serializers.ModelSerializer):
    """Bet serializer."""

    class Meta:
        """Meta."""

        fields = [
            "id",
            "user",
            "lot",
            "amount",
        ]
        model = Bet

    def to_representation(self, instance) -> dict:
        """Transform object."""
        self.fields["user"] = UserSerializer()
        self.fields["lot"] = LotSerializer()
        return super().to_representation(instance)
