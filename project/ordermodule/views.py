from django.shortcuts import render
from ordermodule.models import Category
# Create your views here.
from django.http import HttpResponse


def category(request):
    category = Category.objects.all()
    return render(request, "category.html", {'category': category})


def sample(request, cate_name):
    return render(request, "items.html", {'category': cate_name})
