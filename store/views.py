
from django.db import reset_queries
from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import TemplateView,ListView
from datetime import date
from django.views.generic.edit import CreateView # new
from django.http import JsonResponse
import json
from .models import *
import datetime




 
def home(request):
    '''
    model = Product
    template_name = 'store/store.html'  
    context_object_name = "products_list"
    '''
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created =Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0,'get_cart_total1':0,'shipping':False}
        cartItems=order['get_cart_items']
    
    products=Product.objects.all()
    context={'products':products,'cartItems':cartItems}
    return render(request,'store/store.html',context)     
    
    
    
        
        

'''
class AboutPageView(TemplateView):
    model=OrderItem
    template_name = 'store/cart.html'   
    context_object_name = "orderitem_list"
'''
def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created =Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0,'get_cart_total1':0}
        cartItems=order['get_cart_items']
    context={'items':items,'order':order, 'cartItems': cartItems,'shipping':False}
    return render(request,'store/cart.html',context)     
    


def checkout(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created =Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0,'get_cart_total1':0,'shipping':False}
        cartItems=order['get_cart_items']
    context={'items':items,'order':order,'cartItems': cartItems}
    return render(request,'store/checkout.html',context)     
    
    
    


class RegisterView(CreateView):
    model = Customer
    template_name = "store/register.html"
    fields = ["name","email","birthDate"]
    

def updateItem(request):
    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']
    print('action',action)
    print('productId',productId)
    
    
    customer=request.user.customer
    product=Product.objects.get(id=productId)
    order,created =Order.objects.get_or_create(customer=customer,complete=False)
    orderItem,created =OrderItem.objects.get_or_create(order=order,product=product)
    if action=='add':
        orderItem.quantity=(orderItem.quantity+1)
    else:
        orderItem.quantity=(orderItem.quantity-1)
    
    orderItem.save()
    if orderItem.quantity <=0 :
        orderItem.delete()
        
        
    return JsonResponse('item was added',safe=False)


def processOrder(request):
    transaction_id=datetime.datetime.now().timestamp()
    data=json.loads(request.body)
    if (request.user.is_authenticated):
        customer=request.user.customer
        order,created =Order.objects.get_or_create(customer=customer,complete=False)
        total1=float(data['form']['total1'])
        order.transactionId=transaction_id
        if (total1==order.get_cart_total1):
            order.complete=True
        order.save()
        if (order.shipping==True):
            ShippingAdress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
            country=data['shipping']['country'],
            )
    else:
        print('user is not logged in')
    return JsonResponse('payment complete!',safe=False)

    