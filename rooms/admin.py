from django.contrib import admin
from .models import Room, Reservation


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "capacity", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name", "location")


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("title", "room", "organizer", "start_at", "end_at", "status")
    list_filter = ("status", "room")