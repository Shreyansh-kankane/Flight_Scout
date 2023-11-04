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
                
                # arrayofFlight += MakeMyTrip(source,destination,adults,children,infants,day,month,year)
                # arrayofFlight += GoIbibo(source,destination,adults,children,infants,day,month,year)
                # arrayofFlight += Ixigo(source,destination,adults,children,infants,day,month,year)
                # arrayofFlight += Yatra(source,destination,adults,children,infants,day,month,year)
            finally:
                arrayofFlight = [{'source': 'MakeMytrip', 'flightName': 'Air India Express', 'deptTime': '05:15', 'arrivalTime': '13:45', 'price': '6250', 'URL': 'https://www.makemytrip.com/flight/reviewDetails/?itineraryId=5b18402c6ec41e01437cd60906c383844c812b56&crId=3e17f9f9-540f-4064-afcd-eddf1e56b746&cur=INR&rKey=RKEY:9a26d117-d9ea-4eb2-9a06-775564b32f52:8_0&ccde=IN&xflt=eyJjIjoiRSIsInAiOiJBLTFfQy0wX0ktMCIsInQiOiIiLCJzIjoiREVMLUJMUi0yMDIzMTExNiIsIkl0aW5lcmFyeUlkIjoiREVMLUJMUi0xNi8xMS8yMDIzIiwiVHJpcFR5cGUiOiJPIiwiUGF4VHlwZSI6IkEtMV9DLTBfSS0wIiwiSW50bCI6ZmFsc2UsIkNhYmluQ2xhc3MiOiJFIiwiQ2NkZSI6ImluIiwiUGZ0IjoiIiwiUGFmcyI6IiIsIkZvcndhcmRGbG93UmVxdWlyZWQiOnRydWUsIkNtcElkIjoiIn0='},
                                 {'source': 'MakeMytrip', 'flightName': 'IndiGo', 'deptTime': '02:30', 'arrivalTime': '08:45', 'price': '6977', 'URL': 'https://www.makemytrip.com/flight/reviewDetails/?itineraryId=56b3a5dba2727ec3daec0e825f72ec1e0e0dbc3e&crId=3e17f9f9-540f-4064-afcd-eddf1e56b746&cur=INR&rKey=RKEY:9a26d117-d9ea-4eb2-9a06-775564b32f52:16_0&ccde=IN&xflt=eyJjIjoiRSIsInAiOiJBLTFfQy0wX0ktMCIsInQiOiIiLCJzIjoiREVMLUJMUi0yMDIzMTExNiIsIkl0aW5lcmFyeUlkIjoiREVMLUJMUi0xNi8xMS8yMDIzIiwiVHJpcFR5cGUiOiJPIiwiUGF4VHlwZSI6IkEtMV9DLTBfSS0wIiwiSW50bCI6ZmFsc2UsIkNhYmluQ2xhc3MiOiJFIiwiQ2NkZSI6ImluIiwiUGZ0IjoiIiwiUGFmcyI6IiIsIkZvcndhcmRGbG93UmVxdWlyZWQiOnRydWUsIkNtcElkIjoiIn0='},
                                 {'source': 'MakeMytrip', 'flightName': 'IndiGo', 'deptTime': '21:20', 'arrivalTime': '00:20', 'price': '6982', 'URL': 'https://www.makemytrip.com/flight/reviewDetails/?itineraryId=0375025b468839aac098dda082e6720ba0455101&crId=3e17f9f9-540f-4064-afcd-eddf1e56b746&cur=INR&rKey=RKEY:9a26d117-d9ea-4eb2-9a06-775564b32f52:48_0&ccde=IN&xflt=eyJjIjoiRSIsInAiOiJBLTFfQy0wX0ktMCIsInQiOiIiLCJzIjoiREVMLUJMUi0yMDIzMTExNiIsIkl0aW5lcmFyeUlkIjoiREVMLUJMUi0xNi8xMS8yMDIzIiwiVHJpcFR5cGUiOiJPIiwiUGF4VHlwZSI6IkEtMV9DLTBfSS0wIiwiSW50bCI6ZmFsc2UsIkNhYmluQ2xhc3MiOiJFIiwiQ2NkZSI6ImluIiwiUGZ0IjoiIiwiUGFmcyI6IiIsIkZvcndhcmRGbG93UmVxdWlyZWQiOnRydWUsIkNtcElkIjoiIn0='},
                                 {'source': 'MakeMytrip', 'flightName': 'Vistara', 'deptTime': '18:40', 'arrivalTime': '15:55', 'price': '7167', 'URL': 'https://www.makemytrip.com/flight/reviewDetails/?itineraryId=abe09bdca74ef2f1e2a604bcf85b07be2301f9ec&crId=3e17f9f9-540f-4064-afcd-eddf1e56b746&cur=INR&rKey=RKEY:9a26d117-d9ea-4eb2-9a06-775564b32f52:51_0&ccde=IN&xflt=eyJjIjoiRSIsInAiOiJBLTFfQy0wX0ktMCIsInQiOiIiLCJzIjoiREVMLUJMUi0yMDIzMTExNiIsIkl0aW5lcmFyeUlkIjoiREVMLUJMUi0xNi8xMS8yMDIzIiwiVHJpcFR5cGUiOiJPIiwiUGF4VHlwZSI6IkEtMV9DLTBfSS0wIiwiSW50bCI6ZmFsc2UsIkNhYmluQ2xhc3MiOiJFIiwiQ2NkZSI6ImluIiwiUGZ0IjoiIiwiUGFmcyI6IiIsIkZvcndhcmRGbG93UmVxdWlyZWQiOnRydWUsIkNtcElkIjoiIn0='},
                                 {'source': 'MakeMytrip', 'flightName': 'IndiGo', 'deptTime': '07:00', 'arrivalTime': '09:50', 'price': '7297', 'URL': 'https://www.makemytrip.com/flight/reviewDetails/?itineraryId=a3ecd780ebc1de1b000e337449d05e7a4c8ac7c1&crId=3e17f9f9-540f-4064-afcd-eddf1e56b746&cur=INR&rKey=RKEY:9a26d117-d9ea-4eb2-9a06-775564b32f52:33_0&ccde=IN&xflt=eyJjIjoiRSIsInAiOiJBLTFfQy0wX0ktMCIsInQiOiIiLCJzIjoiREVMLUJMUi0yMDIzMTExNiIsIkl0aW5lcmFyeUlkIjoiREVMLUJMUi0xNi8xMS8yMDIzIiwiVHJpcFR5cGUiOiJPIiwiUGF4VHlwZSI6IkEtMV9DLTBfSS0wIiwiSW50bCI6ZmFsc2UsIkNhYmluQ2xhc3MiOiJFIiwiQ2NkZSI6ImluIiwiUGZ0IjoiIiwiUGFmcyI6IiIsIkZvcndhcmRGbG93UmVxdWlyZWQiOnRydWUsIkNtcElkIjoiIn0='},
                                 {'source': 'GoIbibo', 'flightName': 'Air India Express', 'deptTime': '05:15', 'arrivalTime': '13:45', 'price': '6250', 'URL': 'https://www.goibibo.com/flight-review/?t=1f007b1615faaf665f93f2fc34ed763f6b17457e'},
                                 {'source': 'GoIbibo', 'flightName': 'IndiGo', 'deptTime': '02:30', 'arrivalTime': '08:45', 'price': '6977', 'URL': 'https://www.goibibo.com/flight-review/?t=69f58db49fd19777d3666121369aed7241f47589'},
                                 {'source': 'GoIbibo', 'flightName': 'IndiGo', 'deptTime': '21:20', 'arrivalTime': '00:20', 'price': '6982', 'URL': 'https://www.goibibo.com/flight-review/?t=3bcadd38065885923359bed65be63ae7d4a598f7'},
                                 {'source': 'GoIbibo', 'flightName': 'Vistara', 'deptTime': '18:40', 'arrivalTime': '15:55', 'price': '7167', 'URL': 'https://www.goibibo.com/flight-review/?t=7f43128fbb88bf03b4ee69645850d545b30ed7a3'},
                                 {'source': 'GoIbibo', 'flightName': 'IndiGo', 'deptTime': '07:00', 'arrivalTime': '09:50', 'price': '7297', 'URL': 'https://www.goibibo.com/flight-review/?t=fb05bd40df50e72e36a4ba6550ffe0ae894d2b20'},
                                 {'source': 'Ixigo', 'flightName': 'AIR-INDIA EXPRESS', 'deptTime': '05:15', 'arrivalTime': '13:45', 'price': '6250', 'URL': 'https://www.ixigo.com/flight/booking/1044/new-1q4h34ohdzddtshhdhphphqhh96ohpkddtptsdtkkdvkpp?fareKey=DEL-COK-I5791*COK-BLR-I5972&providers=1044&hbo=false&ftk=DEL%7CBLR%7C161123%7C%7C1%7C0%7C0%7Ce%7CINR%7C04112023124325506%241044%7CDEL-COK-I5791*COK-BLR-I5972%7Cfalse%7Ctrue%7C9250220.0~6250.0~9255965.0~9255810.0~9249715.0&source=Search%20Form'},
                                 {'source': 'Ixigo', 'flightName': 'VISTARA', 'deptTime': '18:40', 'arrivalTime': '15:55', 'price': '7167', 'URL': 'https://www.ixigo.com/flight/booking/1044/new-1q4h34ohdzddtshhdhphphqhh96ohpkddtptsdtkvspktt?fareKey=DEL-GOI-UK855*GOI-BLR-UK882&providers=1044&hbo=false&ftk=DEL%7CBLR%7C161123%7C%7C1%7C0%7C0%7Ce%7CINR%7C04112023124325506%241044%7CDEL-GOI-UK855*GOI-BLR-UK882%7Cfalse%7Ctrue%7C9250541.0~7167.0~9256882.0~9256385.0~9249715.0&source=Search%20Form'},
                                 {'source': 'Ixigo', 'flightName': 'INDIGO', 'deptTime': '21:20', 'arrivalTime': '00:20', 'price': '6982', 'URL': 'https://www.ixigo.com/flight/booking/1044/new-1q4h34ohdzddtshhdhphphqhh96ohpkddtptsdtkzkwkdz?fareKey=DEL-BLR-6E2216&providers=1044&hbo=false&ftk=DEL%7CBLR%7C161123%7C%7C1%7C0%7C0%7Ce%7CINR%7C04112023124325506%241044%7CDEL-BLR-6E2216%7Cfalse%7Ctrue%7C9250144.0~6982.0~9256697.0~9256587.0~9249715.0&source=Search%20Form'},
                                 {'source': 'Ixigo', 'flightName': 'INDIGO', 'deptTime': '07:00', 'arrivalTime': '09:50', 'price': '7297', 'URL': 'https://www.ixigo.com/flight/booking/1044/new-1q4h34ohdzddtshhdhphphqhh96ohpkddtptsdtkupkktv?fareKey=DEL-BLR-6E6403&providers=1044&hbo=false&ftk=DEL%7CBLR%7C161123%7C%7C1%7C0%7C0%7Ce%7CINR%7C04112023124325506%241044%7CDEL-BLR-6E6403%7Cfalse%7Ctrue%7C9250160.0~7297.0~9257012.0~9256896.0~9249715.0&source=Search%20Form'},
                                 {'source': 'Ixigo', 'flightName': 'AIR-INDIA EXPRESS', 'deptTime': '10:35', 'arrivalTime': '17:35', 'price': '7402', 'URL': 'https://www.ixigo.com/flight/booking/1044/new-1q4h34ohdzddtshhdhphphqhh96ohpkddtptsdtkntdszv?fareKey=DEL-IXB-I5552*IXB-BLR-I51531&providers=1044&hbo=false&ftk=DEL%7CBLR%7C161123%7C%7C1%7C0%7C0%7Ce%7CINR%7C04112023124325506%241044%7CDEL-IXB-I5552*IXB-BLR-I51531%7Cfalse%7Ctrue%7C9250258.0~7402.0~9257117.0~9256924.0~9249715.0&source=Search%20Form'}]
                arrayofFlight = sorted(arrayofFlight, key=lambda k: k['price'])
                jsonofFlight=json.dumps(arrayofFlight)
   
                # print(jsonofFlight)
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(elapsed_time)
            
            return render(request, 'results.html', {'flights': arrayofFlight})
            
            
        else:
            form = FlightReservationForm()

    return render(request, 'index.html', {'form': DateInputForm})


 



  
    

    
    



