# from ckeditor.fields import RichTextField
from django.db import models
import os

def upload_to_images(instance, filename):
    # Define the directory where the image will be uploaded
    upload_directory = "static/images"

    # Get the filename extension from the uploaded file
    # extension = os.path.splitext(filename)[1]

    # Construct the final path using the model's primary key and the filename
    # print(f"instance: {instance.pk}")
    # print(f"extension: {extension}")
    final_filename = f"{filename}"
    return os.path.join(upload_directory, final_filename)



class Train(models.Model):
    # Train
    name = models.CharField(max_length=255, null=False)
    capacity = models.IntegerField(null=False)
    date = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to=upload_to_images, blank=True)



    def __str__(self):
        return "{} ({})".format(self.name, self.capacity)



class Station(models.Model):
    # Station
    name = models.CharField(max_length=255, null=False)
    date = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to=upload_to_images, blank=True)



    def __str__(self):
        return "{}".format(self.name)



class TrainClass(models.Model):
    # Station
    name = models.CharField(max_length=255, null=False)
    price = models.IntegerField(null=False)
    date = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to=upload_to_images, blank=True)



    def __str__(self):
        return "{} - {}".format(self.name, self.price)


