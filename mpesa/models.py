from django.db import models

# Create your models here.


# Create your models here.
class Mpesa(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=100, blank=True, default='')
    amount = models.CharField(max_length=100, blank=True, default='')
    payBill = models.CharField(max_length=100, blank=True, default='')
    
    class Meta:
        ordering = ('created',)


