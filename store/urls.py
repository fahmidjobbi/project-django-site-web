from django.http.response import HttpResponse
from django.urls import path
from store.views import    RegisterView
from . import views










urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout , name='checkout'),
    path('',views.home  , name="home"),
    path('register/', RegisterView.as_view() , name="register"),
    path('update_item/', views.updateItem , name="update_item"),
    path('process_order/', views.processOrder , name="process_order"),
   
]    
    

#comment 