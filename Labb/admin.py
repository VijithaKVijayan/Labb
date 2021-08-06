from services.models import Service
from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path
from django.contrib.auth.models import User
from result.models import Result

class MyAdmin(admin.sites.AdminSite):
    site_header = 'SAEDOO'
    site_title = 'SAEDOO'
    index_title = 'SAEDOO'
    site_header_color = "green"
    module_caption_color = "#264B5D"

    def each_context(self, request) :
        context = super().each_context(request)
        context['total_users'] = len(User.objects.all())
        context["site_title"] = getattr(self, "site_title", None)
        context["site_header_color"] = getattr(self, "site_header_color", None)
        context["module_caption_color"] = getattr(self, "module_caption_color", None)
        return context
    
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('graph/<slug:name>/<int:service_id>/', self.admin_view(self.get_user_graphs), name = 'graph'),
        ]
        return my_urls + urls
    
    def get_user_graphs(self, request, name, service_id):
        user = User.objects.get(username = name)
        results = user.result_set.filter(service_id = service_id)
        service_name = Service.objects.get(id = service_id).name
        x_values = [result.value for result in results] # result 
        y_values = [i for i in range(1, len(results) + 1)] # number of times the user get result

        context = dict(
            self.each_context(request),
            title = f'{user.username} graphs for {service_name} check',
            x_values = x_values,
            y_values = y_values,
            service_name = service_name,
        )
        return TemplateResponse(request, 'user_graphs.html', context)

    # def index(self, request, extra_context = None):
    #     user_graph = {
    #         'link': 'graph/',
    #         'name': 'User_graphs'
    #     }
    #     if not extra_context:
    #         extra_context = {}
    #     extra_context = {"user_graph" : user_graph}
    #     return super().index(request, extra_context=extra_context)

myadmin = MyAdmin('admin')

myadmin.register(User)