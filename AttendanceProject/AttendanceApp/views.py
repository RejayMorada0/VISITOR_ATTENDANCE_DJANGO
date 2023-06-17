from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from .models import *

import csv
import qrcode
import os
import time
from datetime import datetime

# filter "AND,OR,NOT"
from django.db.models import Q, Count, Sum

# Create your views here.
installed_apps = ['AttendanceApp']



def visitor(request):
    return render(request, 'AttendanceApp/visitor.html')


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
 
