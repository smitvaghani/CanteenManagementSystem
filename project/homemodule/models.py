from django.db import models

# Create your models here.


class item(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to="pic")
    price = models.FloatField()
    desc = models.TextField()
    category = models.CharField(max_length=20)
    offer = models.BooleanField(default=False)
    discount = models.IntegerField(null=True)


class feedback(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    phone = models.CharField(max_length=10)
    message = models.TextField()
