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

    @property
    def total_amount(self):
        amount = 0.0
        tax = 5
        total_amount = 0.0
        discount = 0
        cart=Cart.objects.filter(user=self.user.id)

        for p in cart:
            temp = (p.quantity * p.item.price * p.item.discount) / 100
            tempamount = ((p.quantity * p.item.price) - temp)
            amount += tempamount
            discount += temp
        total_amount = amount + (amount * tax / 100)

        order={'Amount':amount,'Discount':discount,'Tax (in percentage)':tax,'Total Amount':total_amount}
        return order
