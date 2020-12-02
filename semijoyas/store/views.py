from django.shortcuts import render
from django.http import JsonResponse
import json

from .models import *

# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/home.html', context)

def product(request):
    products = Product.objects.all()
    #categorias =
    context = {'products':products, 'categorias':categorias}
    return render(request, 'store/product.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    context = {'items':items, 'order':order}
    return render(request, 'store/cart.html', context)

def howto(request):
    context = {}
    return render(request, 'store/howto.html', context)

def contact(request):
    context = {}
    return render(request, 'store/contact.html', context)

def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {"product": product}
    return render(request, 'store/product-detail.html', context)

def category(request, categoria):
    product = Product.objects.get(categoria=categoria)
    context = {"product": product}
    return render(request, 'store/categoria.html', context)




def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action: ', action)
    print('Product: ', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <=0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)
