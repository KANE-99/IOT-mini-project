from django.db import models

# Create your models here.
class Data(models.Model):
    temperature = models.CharField(max_length=10,blank=True,null=True)
    humidity = models.CharField(max_length=10,blank=True,null=True)
    flame = models.CharField(max_length=10,blank=True,null=True)
    smoke = models.CharField(max_length=10,blank=True,null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)