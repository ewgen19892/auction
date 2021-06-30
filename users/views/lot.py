"""Lots views."""
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

from users.models.lot import Lot
from users.permissions import LotPermission
from users.serializers.lot import LotSerializer


class LotList(GenericAPIView, ListModelMixin, CreateModelMixin):
    """Lot list view."""

    queryset = Lot.objects.all()
    serializer_class = LotSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs) -> Response:
        """
        Get lots list.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs) -> Response:
        """
        Create a new lot.
        """
        return self.create(request, *args, **kwargs)


class LotDetail(
        GenericAPIView,
        RetrieveModelMixin,
        UpdateModelMixin,
        DestroyModelMixin,
):
    """Lot detail view."""

    serializer_class = LotSerializer
    queryset = Lot.objects.all()
    permission_classes = (IsAuthenticated, LotPermission,)

    def get(self, request, *args, **kwargs) -> Response:
        """
        Get lot by ID.
        """
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs) -> Response:
        """
        Partial lot update with this id.
        """
        return self.partial_update(request, *args, **kwargs)
