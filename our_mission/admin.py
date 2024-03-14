from django.contrib import admin
from .models import Our_Mission
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Our_Mission)
class Our_MissionAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)

# Register your models here.
