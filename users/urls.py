"""Users URL Configuration."""
from django.urls import path

from users.views import UserDetail, UserList
from users.views.bet import BetList, BetDetail
from users.views.lot import LotList, LotDetail

app_name = "users"
urlpatterns = [

    path("users/", UserList.as_view(), name="user_list"),
    path("users/<slug:pk>/", UserDetail.as_view(), name="user_detail"),
    path("bets/", BetList.as_view(), name="bet_list"),
    path("bets/<slug:pk>/", BetDetail.as_view(), name="bet_detail"),
    path("lots/", LotList.as_view(), name="lot_list"),
    path("lots/<slug:pk>/", LotDetail.as_view(), name="lot_detail"),

]
