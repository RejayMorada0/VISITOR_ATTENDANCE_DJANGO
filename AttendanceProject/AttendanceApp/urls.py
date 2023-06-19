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
    path('add_staff', views.add_staff, name='add_staff'),
    path('staff_acc_cvs', views.staff_acc_cvs, name='staff_acc_cvs'),
    path('search_qrcode', views.search_qrcode, name='search_qrcode'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)