
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static #Websites generally need to serve additional files such as images, JavaScript, or CSS
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),  
    path('',include('store.urls')), #to make default home path 
   
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
