from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from .models import *

import csv
import qrcode
import uuid
import os
import os.path
import time
from datetime import datetime
from PIL import Image

# filter "AND,OR,NOT"
from django.db.models import Q, Count, Sum

# Create your views here.
installed_apps = ['AttendanceApp']
 

def guard(request):
    return render(request, 'AttendanceApp/guard.html')

def add_staff(request):
    if request.method=='POST':
        staff_name = request.POST.get('staff_name')
        which_department = request.POST.get('which_department')
        data = Staffs.objects.create(staff_name = staff_name, which_department = which_department)
        data.save()
        messages.success(request, 'Successfully added the staff.')
        return redirect('/guard')

def visitor(request):
    staff = Staffs.objects.all()
    if request.method=='POST':
        rfid = str(uuid.uuid4())[:8] # Generate a unique RFID value (e.g., first 8 characters of a UUID)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        contact_number  = request.POST.get('contact_number')
        person_to_visit = request.POST.get('person_to_visit')
        purpose = request.POST.get('purpose')
        picture = request.FILES["picture"]
        data = Visitors.objects.create(rfid = rfid, first_name = first_name, last_name = last_name, contact_number = contact_number, person_to_visit_id = person_to_visit, purpose = purpose, picture = picture, status = '')
        data.save()

        # BATS START
        qr = qrcode.make(str(rfid))

        # QR code save path / file directory
        location = os.path.join('media/pictures')

        # QR code saved
        qr.save(os.path.join(location,rfid + ".png"))

        # change link when deployed
        os.startfile("http://127.0.0.1:8000/media/pictures/"+rfid+".png")

        # BATS END
        messages.success(request, 'Successfully registered.')
        return redirect('/visitor')

    context = {'staff':staff}
    return render(request, 'AttendanceApp/visitor.html', context)

 
