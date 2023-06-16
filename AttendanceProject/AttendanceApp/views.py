from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from .models import *

import csv

import os
import time
from datetime import datetime

# filter "AND,OR,NOT"
from django.db.models import Q, Count, Sum

# Create your views here.
installed_apps = ['AttendanceApp']



def visitor(request):
    return render(request, 'AttendanceApp/visitor.html')
 