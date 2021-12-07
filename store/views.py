
from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import TemplateView,ListView
from datetime import date
from django.views.generic.edit import CreateView # new

from .models import *



 
class HomePageView(ListView):
    model = Product
    template_name = 'store/store.html'  
    context_object_name = "products_list"


class AboutPageView(TemplateView):
    template_name = 'store/cart.html'


class CheckoutView(TemplateView):
    template_name = 'store/checkout.html'


class RegisterView(CreateView):
    model = Customer
    template_name = "store/register.html"
    fields = ["name","email","birthDate"]
    
