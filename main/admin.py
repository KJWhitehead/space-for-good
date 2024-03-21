from django.contrib import admin
from .models import Reservation
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Reservation)
