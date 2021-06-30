"""Pets views."""
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from pets.models import Pet
from pets.permissions import PetPermission
from pets.serializers import PetSerializer


class PetList(GenericAPIView, ListModelMixin, CreateModelMixin):
    """Pet list view."""

    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        Get queryset.

        :return: Filtered queryset
        """
        return Pet.objects.filter(owner_id=self.request.user.id)

    def get(self, request, *args, **kwargs) -> Response:
        """
        Get pets list.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs) -> Response:
        """
        Create a new pet.
        """
        return self.create(request, *args, **kwargs)


class PetDetail(
        GenericAPIView,
        RetrieveModelMixin,
        UpdateModelMixin,
        DestroyModelMixin,
):
    """Pet detail view."""

    serializer_class = PetSerializer
    queryset = Pet.objects.all()
    permission_classes = (IsAuthenticated, PetPermission,)

    def get(self, request, *args, **kwargs) -> Response:
        """
        Get pet by ID.
        """
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs) -> Response:
        """
        Partial pet update with this id.
        """
        return self.partial_update(request, *args, **kwargs)
