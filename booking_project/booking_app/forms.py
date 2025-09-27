from django.contrib.auth.models import User
from django import forms
from .models import Booking
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["customer", "room", "check_in", "check_out"]
        widgets = {
            "check_in": forms.DateInput(attrs={"type": "date", "placeholder": "YYYY-MM-DD"}),
            "check_out": forms.DateInput(attrs={"type": "date", "placeholder": "YYYY-MM-DD"}),
        }
