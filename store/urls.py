from django.http.response import HttpResponse
from django.urls import path
from store.views import   HomePageView, RegisterView
from . import views










urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout , name='checkout'),
    path('', HomePageView.as_view() , name="home"),
    path('register/', RegisterView.as_view() , name="register"),
    path('update_item/', views.updateItem , name="update_item"),
   
]    
    

#comment 