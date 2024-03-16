from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ('space', 'date', 'time')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
