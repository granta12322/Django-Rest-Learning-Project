from django.db import models
from django.db.models import DateTimeField

class Event(models.Model):
    name = models.CharField(max_length= 200, null = False)
    venue = models.CharField(max_length= 200, null = False, default = "9 Bruce Street")
    start_time = models.DateTimeField(null = False, default = "09/11/2022")
    creation_date = models.DateField(auto_now_add=True)