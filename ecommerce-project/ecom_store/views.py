from django.shortcuts import render, redirect
from django.http  import HttpResponse
from .models import Product, Order
import datetime
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.

def cartItems(cart):
    items = []
    for item in cart:
        items.append(Product.objects.get(id=item))
    return items

def priceCart(cart):
    items = cartItems(cart)
    price=0
    for item in items:
        price = price+item.price
    return price

def catalog(request):
    if 'cart' not in request.session:
        request.session['cart']=[]
    cart = request.session['cart']
    request.session.set_expiry(0)
    store_items = Product.objects.all()
    context = {'store_items' : store_items, 'cart_items' : len(cart)}
    if request.method == "POST":
        cart.append(request.POST['obj_id'])
        return redirect('catalog')
    return render(request, "catalog.html" , context)

def cart(request):
    cart = request.session['cart']
    request.session.set_expiry(0)
    context = {'cart' : cart, 'cart_size' : len(cart), 'cart_items': cartItems(cart), 'total_price':priceCart(cart)}
    return render(request, 'cart.html', context)


def removeCart(request):
    cart = request.session['cart']
    request.session.set_expiry(0)
    id1 = str(request.POST['obj_id'])
    index1 = request.session['cart'].index(id1)
    request.session['cart'].pop(index1)
    return redirect('cart')

def checkout(request):
    request.session.set_expiry(0)
    cart = request.session['cart']
    context = { 
        'cart' : cart, 
        'cart_items' : cartItems(cart),
        'total_price' : priceCart(cart),
        'cart_size' : len(cart)
    }
    return render(request,'checkout.html',context)

def completeOrder(request):
    request.session.set_expiry(0)
    cart = request.session['cart']
    order_details = Order()
    order_details.first_name = request.POST['first_name']
    order_details.last_name = request.POST['last_name']
    order_details.email = request.POST['email']
    order_details.mobile_no = request.POST['mobile']
    order_details.address = request.POST['address']
    order_details.city = request.POST['city']
    order_details.pin_code = request.POST['pin_code']
    order_details.payment_date = datetime.datetime.now()
    cart_items = cartItems(cart)
    items = ''
    for item in cart_items:
        items= items + str(item)
        items= items +"\n"
    order_details.items = items
    order_details.save()
    request.session['cart'] = []
    return render(request,'complete.html')

def adminLoginPage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        users = authenticate(username=username,password=password)
        if users is not None:
            login(request, users)
            return redirect('admin')
        else:
            return render(request,'admin_login.html', {"login":False})
    return render(request, 'admin_login.html', {'login':True})

@login_required
def adminPage(request):
    order = Order.objects.all()
    return render(request, 'admin_page.html' ,{'orders':order})

def fulFilled(request):
    id1 = request.POST['obj_id']
    Order.objects.filter(id=id1).delete()
    return redirect('admin')