from os import name
from django.urls import path, re_path
from django.conf.urls import static
from django.conf import settings
from django.conf.urls.static import static
from . import views

from .views  import *


app_name = 'AttendanceApp'



urlpatterns = [
    # Login
    path('', views.visitor, name='visitor'),
    path('visitor/', views.visitor, name='visitor'),
    path('guard/', views.guard, name='guard'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)