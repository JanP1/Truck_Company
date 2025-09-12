from django.shortcuts import render
from trucks.models import Truck

def home(request):
    # get the first 5 trucks (or adjust ordering if needed)
    last_departed_truck_list = Truck.objects.order_by(
            "truck_code_number" # for now it is code number, has to be departure time
            )[:5]

    context = {
        "last_departed_truck_list": last_departed_truck_list,
    }
    return render(request, "home.html", context)
