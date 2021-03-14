from django.contrib import admin
from ordermodule.models import Category, OrderPlaced
# Register your models here.
admin.site.register(Category)
admin.site.register(OrderPlaced)
