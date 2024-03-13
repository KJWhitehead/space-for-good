from django.contrib import admin
from .models import Space
from .models import Reservation

# Register your models here.
admin.site.register(Space)
admin.site.register(Reservation)