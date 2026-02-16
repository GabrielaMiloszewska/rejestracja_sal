from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, Reservation
from .forms import ReservationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def room_list(request):
    rooms = Room.objects.filter(is_active=True)
    return render(request, "rooms/room_list.html", {"rooms": rooms})

def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    reservations = room.reservations.filter(status=Reservation.Status.ACTIVE)
    return render(request, "rooms/room_detail.html", {"room": room, "reservations": reservations})

@login_required
def reserve_room(request, pk):
    room = get_object_or_404(Room, pk=pk, is_active=True)

    if request.method == "POST":
        form = ReservationForm(request.POST)

        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.room = room
            reservation.organizer = request.user
            reservation.save()

            return redirect("rooms:detail", pk=room.pk)
    else:
        form = ReservationForm()

    return render(
        request,
        "rooms/reserve_room.html",
        {
            "form": form,
            "room": room,
        },
    )