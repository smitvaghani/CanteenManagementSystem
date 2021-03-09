from django.shortcuts import render
from ordermodule.models import Category
from homemodule.models import item
# Create your views here.
from django.http import HttpResponse


def category(request):
    category = Category.objects.all()
    return render(request, "category.html", {'category': category})


def items(request, cate_name):
    items = item.objects.filter(category=cate_name)
    global cate__name
    cate__name = cate_name
    return render(request, "items.html", {'items': items})


def searchItem(request):
    item_name = request.POST['search']
    items = item.objects.filter(name__contains=item_name, category=cate__name)
    return render(request, "items.html", {'items': items})
