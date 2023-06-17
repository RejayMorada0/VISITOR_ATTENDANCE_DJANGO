from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from .models import *

import csv
import qrcode
import uuid
import os
import time
from datetime import datetime

# filter "AND,OR,NOT"
from django.db.models import Q, Count, Sum

# Create your views here.
installed_apps = ['AttendanceApp']


# def generate_rfid():
#     return str(uuid.uuid4())[:8]  

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
        # Generate QR COde
        def generate_qr_code(data, output_file):
            # Create a QR code instance
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)

            # Add data to the QR code
            qr.add_data(data)
            qr.make(fit=True)

            # Create an image from the QR code
            qr_image = qr.make_image(fill_color="black", back_color="white")

            # Save the image to a file
            qr_image.save(output_file)

        # Usage example
        my_data = rfid  # Replace with your variable or data
        output_file = "qr_code.png"  # Replace with the desired output file name

        context = {'staff':staff, 'output_file': output_file}
        generate_qr_code(my_data, output_file)
        # return render(request, 'AttendanceApp/visitor.html', context)
        return redirect('/visitor')

    context = {'staff':staff}
    return render(request, 'AttendanceApp/visitor.html', context)


def generate_qr_code(reference_id, output_file):
    # Create a QR code instance
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)

    # Add data to the QR code
    qr.add_data(reference_id)
    qr.make(fit=True)

    # Create an image from the QR code
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    qr_image.save(output_file)

# Usage example
reference_id = "ABC123"  # Replace with your reference ID
output_file = "qr_code.png"  # Replace with the desired output file name

generate_qr_code(reference_id, output_file)
 
