from django.shortcuts import render, redirect
from .models import Room, Booking, Customer
from .forms import BookingForm
from .forms import BookingForm


def room_list(request):
    rooms = Room.objects.all()
    return render(request, "room_list.html", {"rooms": rooms})



def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, "booking_list.html", {"bookings": bookings})



def create_booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("booking_list")
    else:
        form = BookingForm()
    return render(request, "create_booking.html", {"form": form})
