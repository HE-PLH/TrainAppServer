from django.db import models
import os

import sys
sys.path.append("..")

from resource.models import Station, Train, TrainClass


class Schedule(models.Model):
    # Schedule
    start = models.DateTimeField(null=False)
    end = models.DateTimeField(null=False)
    from_station = models.ForeignKey(Station, verbose_name=("from_station"),related_name="from_station", on_delete=models.CASCADE)
    to_station = models.ForeignKey(Station, verbose_name=("to_station"),related_name="to_station", on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    train_class = models.ForeignKey(TrainClass, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return "{} to {}, {} - {}".format(self.from_station, self.to_station, self.train_class, self.start, self.end)


