from django.contrib import admin
from .models import Space
from .models import Reservation
from django_summernote.admin import SummernoteModelAdmin

# class SpaceAdmin(SummernoteModelAdmin):

#     list_display = ('space', 'max_capacity', 'space_type')
#     search_fields = ['space']
#     list_filter = ('space_type',)?????
#     prepopulated_fields = {'max_capacity': ('title',)}?????
#     summernote_fields = ('content',)?????

# Register your models here.
admin.site.register(Space)
admin.site.register(Reservation)