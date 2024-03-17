from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, JsonResponse
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
                    'Reservation submitted. We look forward to see you!'
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

    
def delete_booking(request, booking_id):
    # Retrieve the booking object based on the booking ID
    booking = get_object_or_404(Reservation, id=booking_id)
    
    # Verify user authorization (optional)
    if booking.user != request.user:
        messages.error(request, 'You are not authorized to delete this booking.')
        return redirect('facilities:bookings_list')  # Redirect to bookings list or another appropriate page

    # Delete the booking object from the database
    booking.delete()
    # Optional: Provide feedback to the user
    messages.success(request, 'Booking deleted successfully.')
    return JsonResponse({'message': 'Booking deleted successfully'})  # Return JSON response for successful deletion

    # Handle other HTTP methods
    return JsonResponse({'error': 'Method not allowed'}, status=405)  # Return JSON response for method not allowed