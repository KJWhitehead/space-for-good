from django.shortcuts import render
from .models import Facilities

def facilities_info(request):
    """
    Renders Facilities page
    """
    facilities = Facilities.objects.all().order_by('title').first()

    return render(
        request,
        "facilities/facilities.html",
        {"facilities": facilities},
    )

# Create your views here.
