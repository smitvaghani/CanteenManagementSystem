from django.db import models
from django.contrib.auth.models import User
from homemodule.models import item
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to="pic")


STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Pending', 'Pending'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='Pending')

    @property
    def total_cost(self):
        temp = (self.quantity * self.item.price * self.item.discount) / 100
        amount = ((self.quantity * self.item.price) - temp)
        return amount
