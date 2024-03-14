from . import views
from django.urls import path

urlpatterns = [
    path('', views.facilities_info, name='facilities'),
]