from django.shortcuts import render
from homemodule.models import item, feedback
# Create your views here.


def feed_back(request):
    name = request.POST['Name']
    email = request.POST['Email']
    phone = request.POST['Phone']
    message = request.POST['Message']
    feed_user = feedback.objects.create(
        name=name, email=email, phone=phone, message=message)
    feed_user.save()
    return render(request, 'feedback.html')


def index(request):
    items = item.objects.filter(offer=True)
    return render(request, 'index.html', {'item': items})


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def recipe(request):
    items = item.objects.filter(offer=True)
    return render(request, 'recipe.html', {'item': items})
