from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

from Labb import settings
from aboutus.views import Homeviewset, HomeImageviewset, Aboutusviewset, AboutUsImageviewset
from result.views import ResultUploadviewset
from services.views import Serviceviewset,  SubServiceviewset ,SubTimeviewset
from user.views import userviewset

from . import admin

router = DefaultRouter()

router.register('users', userviewset)
router.register('Service', Serviceviewset)
router.register('SubService', SubServiceviewset)
router.register('SubTime', SubTimeviewset)
router.register('ResultUpload', ResultUploadviewset)
router.register('Home', Homeviewset)
router.register('HomeImage', HomeImageviewset)
router.register('Aboutus', Aboutusviewset)
router.register('AboutUsImage', AboutUsImageviewset)

urlpatterns = [
    path('admin/', admin.myadmin.urls, name = 'admin'),
    path('api/', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('summernote/', include('django_summernote.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)