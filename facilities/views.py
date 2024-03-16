from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from .models import Facilities, Space
from .forms import ReservationForm
from .models import Reservation


def facilities_info(request):
    """
    Renders Facilities page
    """
    facilities = Facilities.objects.all().order_by('title').first()
    reservation_form = ReservationForm()

    if request.method == "POST":
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            try:
                reservation = reservation_form.save(commit=False)
                reservation.user = request.user
                reservation.save()
                messages.success(
                    request,
                    'Reservation submitted and awaiting approval.'
                )
            except ValidationError as e:
                messages.error(request, str(e))
        else:
            messages.error(request, 'Please correct the errors.')

    template = "facilities/facilities.html"
    context = {
        "facilities": facilities,
        "reservation_form": reservation_form,
    }
    return render(request, template, context)

def view_bookings(request):
    # Retrieve bookings associated with the current user
    user_bookings = Reservation.objects.filter(user=request.user)
    context = {
        'user_bookings': user_bookings
    }
    return render(request, 'facilities/bookings.html', context)
