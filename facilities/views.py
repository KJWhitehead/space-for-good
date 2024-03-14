from django.shortcuts import render
from .models import Facilities
from .forms import ReservationForm

def facilities_info(request):
    """
    Renders Facilities page
    """
    facilities = Facilities.objects.all().order_by('title').first()
    reservation_form = ReservationForm()

    return render(
        request,
        "facilities/facilities.html",
        {"facilities": facilities,
        "reservation_form": reservation_form},
        
    )

# Create your views here.
