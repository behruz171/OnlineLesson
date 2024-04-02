from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('videos/', video),
    path('videos/<int:pk>', video_detail )
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static( settings.STATIC_URL, document_root=settings.STATIC_ROOT)



