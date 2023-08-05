from django import forms
from .widgets import CustomClearableFileInput
from .models import Service


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = '__all__'
        exclude = ['slug',]

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
