"""Lots serializers."""
from rest_framework import serializers

from pets.serializers import PetSerializer
from users.models.lot import Lot
from users.serializers import UserSerializer


class LotSerializer(serializers.ModelSerializer):
    """Lot serializer."""

    class Meta:
        """Meta."""

        fields = [
            "id",
            "pet",
            "owner",
            "price",
        ]
        model = Lot

    def to_representation(self, instance) -> dict:
        """Transform object."""
        self.fields["owner"] = UserSerializer()
        self.fields["pet"] = PetSerializer()
        return super().to_representation(instance)
