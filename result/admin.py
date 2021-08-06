from django.contrib import admin
from django.utils.html import format_html
from Labb.admin import myadmin

# Register your models here.
from result.models import Result

class ResultAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'service', 'result', 'value', 'graph')
    list_filter = ('service', 'user', 'result', 'value')

    def graph(self, obj):
        if obj.result is None: 
            return format_html(f'<a href="/admin/graph/{obj.user.username}/{obj.service.id}/">See graph</a>')
        return '-'

myadmin.register(Result, ResultAdmin)