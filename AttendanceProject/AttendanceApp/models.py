from django.db import models
from django.db.models import Model
import os

class Visitors(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    contact_number = models.IntegerField(null=True, blank=True)
    person_to_visit = models.ForeignKey("Staffs", on_delete=models.CASCADE)
    purpose = models.CharField(max_length=500, null=True, blank=True)
    picture = models.FileField(upload_to ='pictures/', null=True, blank=True)
  
    class Meta:
        verbose_name_plural = "Visitors" 


class Staffs(models.Model):
    staff_name = models.CharField(max_length=255, null=True, blank=True)
    which_department = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Staffs" 
