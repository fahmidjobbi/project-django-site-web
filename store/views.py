
from django.db import reset_queries
from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import TemplateView,ListView
from datetime import date
from django.views.generic.edit import CreateView # new
from django.http import JsonResponse
import json
from .models import *




 
class HomePageView(ListView):
    model = Product
    template_name = 'store/store.html'  
    context_object_name = "products_list"

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
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0,'get_cart_total1':0}
    context={'items':items,'order':order}
    return render(request,'store/cart.html',context)     
    


def checkout(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created =Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0,'get_cart_total1':0}
    context={'items':items,'order':order}
    return render(request,'store/checkout.html',context)     
    
    
    


class RegisterView(CreateView):
    model = Customer
    template_name = "store/register.html"
    fields = ["name","email","birthDate"]
    

def updateItem(request):
    data=json.loads(request.data)
    productId=data['productID']
    action=data['action']
    print('action',action)
    print('productId',productId)
    return JsonResponse('item was added',safe=False)