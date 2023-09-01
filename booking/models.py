from django.contrib.auth.models import User
from django.db import models
import os

import sys
sys.path.append("..")

from schedule.models import Schedule



class Booking(models.Model):
    # inventory
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    county = models.CharField(null=True, max_length=255, default='Nairobi')
    name = models.CharField(null=False, max_length=255)
    city = models.CharField(null=True, max_length=255, default='Nairobi')
    phone = models.CharField(null=False, max_length=255)
    paid = models.CharField(null=True, max_length=255, default='Not Paid')
    date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return "{} -{} -{}-({})".format(self.id, self.name, self.phone, self.paid)


class BookingItem(models.Model):
    # inventory
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    seats = models.IntegerField(null=False, default=1)
    price = models.IntegerField(null=False, default=1)
    date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return "{} - ({}), {}".format(self.schedule, self.seats,self.price)


