from django import forms
from django.forms import ModelForm
from .models import Booking
from django.core.exceptions import ValidationError
from django.utils import timezone


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    def clean_date(self):
        date = self.cleaned_data['date']
        if date < timezone.now().date():
            raise forms.ValidationError(message='Date cannot be in the past')
        return date

    class Meta:
        model = Booking
        fields = '__all__'
        exclude = ('user_profile',)
        widgets = {'date': DateInput()}
