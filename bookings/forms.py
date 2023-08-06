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
        exclude = ('user_profile', 'status',)
        widgets = {'date': DateInput()}

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Your Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'service': 'Choose treatment',
            'package': 'Choose package',
            'date': 'Prefered date',
            'time': 'Prefered time',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'my-2'
            self.fields[field].label = placeholder
