from django.db import models
from django.db.models import Model
import os
from django.core.validators import RegexValidator

class Visitors(models.Model):
    cellphone_regex = RegexValidator(
        regex=r'^09\d{9}$',
        message="Enter a valid cellphone number."
    )
    
    rfid = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    contact_number = models.CharField(max_length=11, validators=[cellphone_regex])
    person_to_visit = models.ForeignKey("Staffs", on_delete=models.CASCADE)
    purpose = models.CharField(max_length=500, null=True, blank=True)
    picture = models.FileField(upload_to ='pictures/', null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Visitors" 


class Staffs(models.Model):
    staff_name = models.CharField(max_length=255, null=True, blank=True)
    which_department = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Staffs" 
