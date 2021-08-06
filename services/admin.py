from django.contrib import admin
from Labb.admin import myadmin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from services.models import Service, SubService, Booking, BookingLine

myadmin.register(Service)
myadmin.register(SubService)

class BookingLineInLine(admin.TabularInline):
    model = BookingLine
    row_id_fields = ("service", )
    
    def get_extra(self, request, obj=None, **kwargs):
        return 1

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'time_of_result')
    list_editable = ('status', 'time_of_result')
    list_filter = ('status', )
    inlines = (BookingLineInLine, )
    

myadmin.register(Booking, BookingAdmin)
