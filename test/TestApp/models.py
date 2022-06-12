from django.db import models
from django.db.models import DateTimeField

class Event(models.Model):
    name = models.CharField(max_length= 200, null = False)
    venue = models.CharField(max_length= 200, null = False, default = "9 Bruce Street")
    start_time = models.DateTimeField(null = False, default = "2022-09-11 10:00:00")
    creation_date = models.DateField(auto_now_add=True)


class Ticket(models.Model):
    event = models.ForeignKey(to = "Event", on_delete= models.CASCADE)
    ticket_used = models.BooleanField(default = False)
    original_list_price = models.BooleanField(default = 10)
    is_original_listing = models.BooleanField(default = False)
    is_for_sale = models.BooleanField(default= True)
