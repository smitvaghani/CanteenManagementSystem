from django.db import models
from homemodule.models import item
from django.contrib.auth.models import User
# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
