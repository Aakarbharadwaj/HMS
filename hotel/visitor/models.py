from django.db import models

# Create your models here.
class Details(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    Adhar_id = models.CharField(max_length=50)
    Room_no = models.CharField(max_length=50)
    Time_in = models.DateTimeField(auto_now=True)
    Time_out = models.DateTimeField()
    Contact = models.CharField(max_length=20)

