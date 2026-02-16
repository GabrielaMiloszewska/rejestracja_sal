from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Room, Reservation
from .forms import ReservationForm
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

    return render(request,"rooms/reserve_room.html", {"form": form, "room": room,},)

@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(
        organizer=request.user,
        start_at__gte=timezone.now(),
        status=Reservation.Status.ACTIVE,
    ).order_by("start_at")

    return render(request, "rooms/my_reservations.html", {"reservations": reservations})


@login_required
def cancel_reservation(request, pk):
    reservation = get_object_or_404(
        Reservation,
        pk=pk,
        organizer=request.user
    )

    reservation.cancel()
    messages.success(request, "Reservation cancelled.")

    return redirect("rooms:my_reservations")

@login_required
def edit_reservation(request, pk):
    reservation = get_object_or_404(
        Reservation,
        pk=pk,
        organizer=request.user
    )

    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, "Reservation updated.")
            return redirect("rooms:my_reservations")
    else:
        form = ReservationForm(instance=reservation)

    return render(
        request,
        "rooms/reservation_form.html",
        {"form": form, "reservation": reservation},
    )