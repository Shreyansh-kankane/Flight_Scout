from django import forms
from .models import FlightReservation


class FlightReservationForm(forms.ModelForm):
    class Meta:
        model = FlightReservation
        fields = ['departure_city', 'destination_city',
                  'date', 'adults_count', 'children_count', 'infants_count']


class DateInputForm(forms.Form):
    date = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date'})
    )
