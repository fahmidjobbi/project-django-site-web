
from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'store/store.html'


class AboutPageView(TemplateView):
    template_name = 'store/cart.html'


class CheckoutView(TemplateView):
    template_name = 'store/checkout.html'
