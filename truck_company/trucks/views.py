from django.shortcuts import get_object_or_404, render
from .models import Truck

from django.views.generic import ListView

# Create your views here.
def index(request):
    last_departed_truck_list = Truck.objects.order_by(
            "truck_code_number" # this is to be changed. Need to add last departure time 
            )
    context = {"last_departed_truck_list": last_departed_truck_list}
    return render(request, "trucks/index.html", context)

def display_truck_info(request, truck_id):
    truck = get_object_or_404(Truck, pk=truck_id)
    return render(request, "trucks/display_truck_info.html", {"truck": truck})

class TruckListView(ListView):
    model = Truck
    template_name = "trucks/truck_list.html"
    context_object_name = "trucks"

