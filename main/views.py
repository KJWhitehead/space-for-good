from django.shortcuts import render
from django.views import generic
from .models import Space
from .models import Reservation


# Create your views here.
class SpaceList(generic.ListView):
    queryset = Space.objects.all()
    template_name = "post_list.html"

