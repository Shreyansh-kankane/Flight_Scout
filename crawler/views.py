from django.shortcuts import render, redirect
from .forms import DateInputForm
from .forms import FlightReservationForm
from django.http import HttpResponse
from .models import FlightInput
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

def inputs(request):
    if request.method == 'GET':
        queryset = FlightInput.objects.all()
        data_as_list_of_dicts = list(queryset.values())
        print(data_as_list_of_dicts[-1])
        return HttpResponse(data_as_list_of_dicts[-1].values())
