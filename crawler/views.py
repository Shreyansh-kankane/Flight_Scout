from django.shortcuts import render, redirect
from .forms import DateInputForm
from .forms import FlightReservationForm
from django.http import HttpResponse
from .models import FlightInput
import time
import json
from crawlers.Yatra import Yatra
from crawlers.GoIbibo import GoIbibo
from crawlers.Ixigo import Ixigo
from crawlers.MakeMyTrip import MakeMyTrip


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



arrayofFlight=[]

try:
    date=date.split("-")
    source="DEL"
    destination="BOM"
    adults="1" # needs to be str
    children="0"
    infants="0"
    day=date[2]
    month=date[1]
    year=date[0]
    GoIbibo(source,destination,adults,children,infants,day,month,year)
  
finally:
    jsonofFlight=json.dumps(arrayofFlight)

    print(jsonofFlight)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(elapsed_time)

  
    

    
    



