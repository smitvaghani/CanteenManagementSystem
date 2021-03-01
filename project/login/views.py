from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from homemodule.models import item
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            items = item.objects.all()
            return render(request, 'index.html', {'user':user,'item' : items})
        else:
            messages.info(request, 'your username or password is invalid!')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        email = request.POST['email']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Already Username Taken!')
                return render(request, 'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Already email taken!')
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(
                    username=username, password=password, email=email)
                user.save()
                return render(request, 'login.html')
        else:
            messages.info(request, 'password not matching!')
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')

def logout_view(request):
    logout(request)
    items = item.objects.all()
    return render(request, 'index.html',{'item' : items})
    
