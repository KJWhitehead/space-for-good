from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Facilities, Space
from .forms import ReservationForm, EditReservationForm
from .models import Reservation


@login_required
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
                    'Reservation submitted. We look forward to seeing you!'
                )
                return redirect('view_bookings') 
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


@login_required
def view_bookings(request):
    # Retrieve bookings associated with the current user
    user_bookings = Reservation.objects.filter(user=request.user).order_by('date', 'time')
    context = {
        'user_bookings': user_bookings
    }
    return render(request, 'facilities/bookings.html', context)


@login_required
def edit_booking(request, booking_id):
    # Retrieve the booking object based on the booking ID
    booking = get_object_or_404(Reservation, id=booking_id)
    # Verify user authorization
    if booking.user != request.user:
        messages.error(request, 'You are not authorized to edit this booking.')
        return redirect('view_bookings')

    if request.method == 'POST':
        form = EditReservationForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking updated successfully.')
            return redirect('view_bookings')
    else:
        form = EditReservationForm(instance=booking)

    context = {
        'booking': booking,
        'form': form,
    }
    return render(request, 'facilities/edit_booking.html', context)


@login_required    
def delete_booking(request, booking_id):
    # Retrieve the booking object based on the booking ID
    booking = get_object_or_404(Reservation, id=booking_id)
    
    # Verify user authorization 
    if booking.user != request.user:
        messages.error(request, 'You are not authorized to delete this booking.')
        return redirect('view_bookings')  # Redirect to bookings list or another appropriate page

    # Delete the booking object from the database
    booking.delete()
    
    # Provide feedback to the user
    messages.success(request, 'Booking deleted successfully.')
    return redirect('view_bookings')  # Redirect to bookings list or another appropriate page