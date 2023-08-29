from django.db import models
import os

import sys
sys.path.append("..")

from schedule.models import Schedule



class Booking(models.Model):
    # inventory
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    seats = models.IntegerField(null=False, default=1)
    date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return "{} - ({})".format(self.schedule, self.seats)


