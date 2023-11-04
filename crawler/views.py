from django.shortcuts import render, redirect
from .forms import DateInputForm
from .forms import FlightReservationForm
from django.http import HttpResponse
from .models import FlightInput
import time
import json
from .crawlers.Yatra import Yatra
from .crawlers.GoIbibo import GoIbibo
from .crawlers.Ixigo import Ixigo
from .crawlers.MakeMyTrip import MakeMyTrip


def flight_reservation(request):
    if request.method == 'POST':
        form = FlightReservationForm(request.POST)
        if form.is_valid():
            form.save() 
            queryset = FlightInput.objects.all()
            data_as_list_of_dicts = list(queryset.values())
            print(data_as_list_of_dicts[-1])
            arrayofFlight=[]
            start_time = time.time()
            try:
                # Departure
                source=data_as_list_of_dicts[-1]["departure_city"]
                # Destination
                destination=data_as_list_of_dicts[-1]["destination_city"]
                # Date
                date = data_as_list_of_dicts[-1]["date"]
                date = date.strftime('%Y-%m-%d')
                date=date.split("-")
                day=date[2]
                month=date[1]
                year=date[0]
                # Number of passengers
                adults=data_as_list_of_dicts[-1]["adults_count"] 
                children=data_as_list_of_dicts[-1]["children_count"] 
                infants=data_as_list_of_dicts[-1]["infants_count"] 
                
                arrayofFlight += MakeMyTrip(source,destination,adults,children,infants,day,month,year)
                arrayofFlight += GoIbibo(source,destination,adults,children,infants,day,month,year)
                arrayofFlight += Ixigo(source,destination,adults,children,infants,day,month,year)
                arrayofFlight += Yatra(source,destination,adults,children,infants,day,month,year)
            finally:
                jsonofFlight=json.dumps(arrayofFlight)

                print(jsonofFlight)
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(elapsed_time)
            
            return HttpResponse(arrayofFlight)
            
            
        else:
            form = FlightReservationForm()

    return render(request, 'index.html', {'form': DateInputForm})


 



  
    

    
    



