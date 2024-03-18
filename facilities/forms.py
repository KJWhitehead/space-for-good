from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Reservation

def future_date_validator(value):
    if value <= timezone.now().date():
        raise ValidationError('Reservation date must be in the future.')

class ReservationForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), validators=[future_date_validator])
    class Meta:
        model = Reservation
        fields = ('space', 'date', 'time')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        space = cleaned_data.get('space')
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        # Check if there are any existing bookings for the selected space and time
        existing_bookings = Reservation.objects.filter(space=space, date=date, time=time)
        if existing_bookings.exists():
            raise ValidationError('Sorry, this space is already booked for the selected date and time.')

        return cleaned_data

class EditReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('space', 'date', 'time')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }