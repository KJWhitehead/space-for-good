from . import views
from django.urls import path
from .views import view_bookings

urlpatterns = [
    path('', views.facilities_info, name='facilities'),
    path('bookings/', views.view_bookings, name='view_bookings'),
    path('bookings/<int:booking_id>/delete/', views.delete_booking,
         name='delete_booking'),
    path('bookings/<int:booking_id>/edit/', views.edit_booking,
         name='edit_booking'),
]
