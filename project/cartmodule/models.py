from django.db import models
from homemodule.models import item
from django.contrib.auth.models import User
# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        temp = (self.quantity * self.item.price * self.item.discount) / 100
        amount = ((self.quantity * self.item.price) - temp)
        return amount
