from django.http.response import HttpResponse
from django.urls import path
from store.views import AboutPageView, CheckoutView, HomePageView











urlpatterns = [
    path('cart/', AboutPageView.as_view() , name='cart'),
    path('checkout/', CheckoutView.as_view() , name='checkout'),
    path('', HomePageView.as_view() , name="home"),
]    
    

#comment 