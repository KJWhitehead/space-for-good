from . import views
from django.urls import path
from .views import view_bookings

urlpatterns = [
    path('', views.facilities_info, name='facilities'),
    path('bookings/', views.view_bookings, name='view_bookings'),
]