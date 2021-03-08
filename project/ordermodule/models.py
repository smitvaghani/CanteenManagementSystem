from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to="pic")
    
