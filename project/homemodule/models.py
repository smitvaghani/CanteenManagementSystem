from django.db import models

# Create your models here.


class item(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to="pic")
    price = models.FloatField()
    desc = models.TextField()
    category = models.CharField(max_length=20, default="gujarati")
    offer = models.BooleanField(default=False)
    discount = models.IntegerField(default=5)


class feedback(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    phone = models.CharField(max_length=10)
    message = models.TextField()
