from . import views
from django.urls import path

urlpatterns = [
    path('', views.our_mission_sfg, name='our_mission')
]