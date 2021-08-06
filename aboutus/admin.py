from django.contrib import admin
#summer note
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
from aboutus.models import AboutUsImage, HomeImage, Home, Aboutus
@admin.register(Home)
@admin.register(AboutUsImage)
@admin.register(Aboutus)
@admin.register(HomeImage)
class HomeAdmin(SummernoteModelAdmin,admin.ModelAdmin):
    #Admin View for Home

#   list_display = ('description',)
   summernote_fields = ('description','contactdetail')

class HomeImage(SummernoteModelAdmin,admin.ModelAdmin):

 #   list_dispaly=('home',)
   summernote_fields = ('home','img',)

class Aboutus(SummernoteModelAdmin,admin.ModelAdmin):
   #list_display = ('description')
   summernote_fields = ('description')

class AboutUsImage(SummernoteModelAdmin,admin.ModelAdmin):
 #  list_display = ('aboutus',)
   summernote_fields = ('aboutus','img',)

