from django.shortcuts import render, redirect
from .forms import DateInputForm
from .forms import FlightReservationForm
from django.http import HttpResponse
# Create your views here.


def flight_reservation(request):
    if request.method == 'POST':
        print(request.POST)
        form = FlightReservationForm(request.POST)
        if form.is_valid():
            form.save()  # This will save the data to the FlightReservation model
            return HttpResponse('Form submitted successfully')

        else:
            form = FlightReservationForm()

    return render(request, 'index.html', {'form': DateInputForm})
