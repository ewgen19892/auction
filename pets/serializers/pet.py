"""Pets serializers."""
from rest_framework import serializers

from pets.models import Pet
from users.serializers import UserSerializer


class PetSerializer(serializers.ModelSerializer):
    """Pet serializer."""

    class Meta:
        """Meta."""

        fields = [
            "id",
            "breed",
            "nickname",
            "owner",
        ]
        model = Pet
        read_only_fields = (
            "owner",
        )

    def to_representation(self, instance) -> dict:
        """Transform object."""
        self.fields["owner"] = UserSerializer()
        return super().to_representation(instance)
