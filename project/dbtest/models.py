from django.db import models

# Create your models here.


class student(models.Model):
    name = models.CharField(max_length=30)
    emailId = models.CharField(max_length=50)
    rollNo = models.IntegerField()
    dob = models.CharField(max_length=10)
