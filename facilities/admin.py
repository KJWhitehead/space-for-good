from django.contrib import admin
from .models import Facilities
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Facilities)
class FacilitiesAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

# Register your models here.
