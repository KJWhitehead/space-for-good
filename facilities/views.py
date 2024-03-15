from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Facilities, Space
from .forms import ReservationForm


def facilities_info(request):
    """
    Renders Facilities page
    """
    facilities = Facilities.objects.all().order_by('title').first()
    reservation_form = ReservationForm(request.POST or None)
    if request.method == "POST":
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            reservation.author = request.user
            reservation.space = space #?
            reservation.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Reservation submitted and awaiting approval'
            )

    template = "facilities/facilities.html"
    context = {
        "facilities": facilities,
        "reservation_form": reservation_form,
    }
    return render(request, template, context)
