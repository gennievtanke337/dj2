from django.contrib.auth.models import User
from django import forms
from .models import Booking
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Booking, Customer


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["customer", "room", "check_in", "check_out"]
        widgets = {
            "check_in": forms.DateInput(attrs={"type": "date", "placeholder": "YYYY-MM-DD"}),
            "check_out": forms.DateInput(attrs={"type": "date", "placeholder": "YYYY-MM-DD"}),
        }


    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and not user.is_staff:

            self.fields['customer'].queryset = Customer.objects.filter(user=user)
            self.fields['customer'].initial = Customer.objects.get(user=user)
            self.fields['customer'].widget = forms.HiddenInput()