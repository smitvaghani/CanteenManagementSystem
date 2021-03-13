from django.shortcuts import render
from .models import Cart
from homemodule.models import item
from django.contrib.auth.models import User, auth
from django.db.models import Q
from django.http import JsonResponse
# Create your views here.


def add_to_cart(request):
    if request.user.is_authenticated:
        user = request.user
        item_id = request.GET['id']
        items = item.objects.get(id=item_id)
        item_details = item.objects.filter(id=item_id)
        cart = Cart(user=user, item=items)
        cart.save()
        if Cart.objects.filter(item_id=item_id).exists():
            return render(request, 'itemDetails.html', {'is_exists': True, 'item': item_details})
        else:
            return render(request, 'itemDetails.html', {'is_exists': False, 'item': item_details})
    else:
        return render(request, "login.html")


def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        tax = 5
        total_amount = 0.0
        discount = 0
        cart_item = [p for p in Cart.objects.all() if p.user == user]
        if cart_item:
            for p in cart_item:
                temp = (p.quantity * p.item.price * p.item.discount) / 100
                tempamount = ((p.quantity*p.item.price) - temp)
                amount += tempamount
                discount += temp
            total_amount = amount + (amount * tax / 100)
            return render(request, 'cart.html', {'cart': cart, 'total_amount': round(total_amount, 2), 'amount': round(amount, 2), 'tax': tax, 'discount': round(discount, 2)})
        else:
            return render(request, "emptycart.html")
    else:
        return render(request, "login.html")


def plus_cart(request):
    if request.method == 'GET':
        item_id = request.GET['item_id']
        c = Cart.objects.get(Q(item=item_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        tax = 5
        total_amount = 0.0
        discount = 0
        cart_item = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_item:
            temp = (p.quantity * p.item.price * p.item.discount) / 100
            tempamount = ((p.quantity*p.item.price) - temp)
            amount += tempamount
            discount += temp
        total_amount = amount + (amount * tax / 100)
        data = {
            'quantity': c.quantity,
            'total_amount': round(total_amount, 2),
            'amount': round(amount, 2),
            'discount': round(discount, 2),
        }
        return JsonResponse(data)


def minus_cart(request):
    if request.method == 'GET':
        item_id = request.GET['item_id']
        c = Cart.objects.get(Q(item=item_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        tax = 5
        total_amount = 0.0
        discount = 0
        cart_item = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_item:
            temp = (p.quantity * p.item.price * p.item.discount) / 100
            tempamount = ((p.quantity*p.item.price) - temp)
            amount += tempamount
            discount += temp
        total_amount = amount + (amount * tax / 100)
        data = {
            'quantity': c.quantity,
            'total_amount': round(total_amount, 2),
            'amount': round(amount, 2),
            'discount': round(discount, 2),
        }
        return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        item_id = request.GET['item_id']
        c = Cart.objects.get(Q(item=item_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        tax = 5
        total_amount = 0.0
        discount = 0
        cart_item = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_item:
            temp = (p.quantity * p.item.price * p.item.discount) / 100
            tempamount = ((p.quantity*p.item.price) - temp)
            amount += tempamount
            discount += temp
        total_amount = amount + (amount * tax / 100)
        data = {
            'total_amount': round(total_amount, 2),
            'amount': round(amount, 2),
            'discount': round(discount, 2),
        }
        return JsonResponse(data)
