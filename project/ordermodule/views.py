from django.shortcuts import render, redirect
from reportlab.pdfgen import canvas  
from django.http import HttpResponse  
from ordermodule.models import Category, OrderPlaced
from homemodule.models import item
from cartmodule.models import Cart
from django.contrib import messages


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
    items = item.objects.filter(name__icontains=item_name, category=cate__name)
    return render(request, "items.html", {'items': items})


def itemDetails(request, item_id):
    user = request.user
    itemdetails = item.objects.filter(id=item_id)
    if request.user.is_authenticated:
        if Cart.objects.filter(user=user, item_id=item_id).exists():
            return render(request, 'itemDetails.html', {'is_exists': True, 'item': itemdetails})
        else:
            return render(request, 'itemDetails.html', {'is_exists': False, 'item': itemdetails})
    else:
        return render(request, 'itemDetails.html', {'is_exists': False, 'item': itemdetails})


def checkout(request):
    user = request.user
    cart_item = Cart.objects.filter(user=user)
    amount = 0.0
    tax = 5
    total_amount = 0.0
    discount = 0
    cart_item = [p for p in Cart.objects.all() if p.user == request.user]
    if cart_item:
        for p in cart_item:
            temp = (p.quantity * p.item.price * p.item.discount) / 100
            tempamount = ((p.quantity * p.item.price) - temp)
            amount += tempamount
            discount += temp
        total_amount = amount + (amount * tax / 100)
    return render(request, 'checkout.html', {'item': cart_item, 'totalamount': total_amount, 'amount': amount, 'tax': tax, 'discount': discount})


def invoice(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, item=c.item, quantity=c.quantity).save()
        c.delete()
    return redirect('/order/orderdetails')


def orderDetails(request):
    user = request.user
    order = OrderPlaced.objects.filter(user=user)
    return render(request, 'orderdetails.html', {'order': order})

def gen_invoice(request):
    user = request.user
    order = OrderPlaced.objects.filter(user=user)
    return render(request, 'invoice.html',{'order':order})

def preview(request):
    id = request.GET["id"]
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'  
    p = canvas.Canvas(response)  
    p.setFont("Times-Roman", 55)  
    p.drawString(100,700, id)  
    p.showPage()  
    p.save()  
    return response 
