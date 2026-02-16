from django.urls import path
from . import views

app_name = "rooms"

urlpatterns = [
    path("", views.room_list, name="list"),
    path("<int:pk>/", views.room_detail, name="detail"),
    path("<int:pk>/reserve/", views.reserve_room, name="reserve"),
    path("my/", views.my_reservations, name="my_reservations"),
]