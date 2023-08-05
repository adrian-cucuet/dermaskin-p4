from django import forms
from django.forms import ModelForm
from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {'date': DateInput()}
