from django.shortcuts import render, redirect, get_object_or_404
from .models import Room, Booking, Customer
from .forms import BookingForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


@login_required
def room_list(request):
    rooms = Room.objects.all()
    user_bookings = Booking.objects.filter(customer__user=request.user)
    return render(request, "room_list.html", {
        "rooms": rooms,
        "user_bookings": user_bookings
    })


@login_required
def booking_list(request):
    if not request.user.is_staff:
        return redirect("room_list")
    bookings = Booking.objects.all()
    return render(request, "booking_list.html", {"bookings": bookings})


@login_required
def create_booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("booking_list")
    else:
        form = BookingForm(user=request.user)
    return render(request, "create_booking.html", {"form": form})


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.user.is_staff or booking.customer.user == request.user:
        booking.delete()
    return redirect("room_list" if not request.user.is_staff else "booking_list")


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Customer.objects.create(user=user, phone="")
            login(request, user)
            return redirect('room_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('room_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
