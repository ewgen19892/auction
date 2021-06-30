"""Bets views."""
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models.bet import Bet
from users.serializers.bet import BetSerializer


class BetList(GenericAPIView, ListModelMixin, CreateModelMixin):
    """Bet list view."""

    queryset = Bet.objects.all()
    serializer_class = BetSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs) -> Response:
        """
        Get Bets list.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs) -> Response:
        """
        Create a new bet.
        """
        return self.create(request, *args, **kwargs)


class BetDetail(
        GenericAPIView,
        RetrieveModelMixin,
):
    """Bet detail view."""

    serializer_class = BetSerializer
    queryset = Bet.objects.all()
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs) -> Response:
        """
        Get bet by ID.
        """
        return self.retrieve(request, *args, **kwargs)
