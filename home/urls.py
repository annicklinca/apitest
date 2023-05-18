from django.urls import path
from .import views

from .views import *
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from . import views
urlpatterns = [
    path('', views.welcome, name='home'),                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    path('api/product/', views.addproduct,name='Product'), 


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
