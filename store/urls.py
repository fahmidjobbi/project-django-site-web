from django.http.response import HttpResponse
from django.urls import path
from store.views import AboutPageView, CheckoutView, HomePageView, RegisterView











urlpatterns = [
    path('cart/', AboutPageView.as_view() , name='cart'),
    path('checkout/', CheckoutView.as_view() , name='checkout'),
    path('', HomePageView.as_view() , name="home"),
    path('register/', RegisterView.as_view() , name="register"),
   
]    
    

#comment 