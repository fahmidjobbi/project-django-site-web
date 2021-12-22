from django.db import models
from django.db.models.expressions import F
from django.db.models.fields import CharField, Field
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

# Create your models here.




class Invoice(models.Model):
    class PayementMode(models.TextChoices):
        CASH='CS', _("Cash")
        DEBIT_CARD='DC', _("Debit card")
        WIRE_TRANSFER='WT', _("Wire transfer")
        
    class Meta:
            db_table="invoices"
        
    
    payementMode=models.CharField(
        max_length=2,
        choices=PayementMode.choices,
        default=PayementMode.CASH)


    
class Category(models.Model):
    name=models.CharField(max_length=200,null=True)
    description=models.TextField()

    class Meta:
            db_table="categories"
        
    
    def __str__(self):
        return self.name


class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,null=True)
    email=models.EmailField()
    birthDate=models.DateField()
    
    class Meta:
            db_table="customers"
        
    
    def __str__(self):
        return self.name +"--------"+ self.email 




class Product(models.Model):
    name=models.CharField(max_length=200,null=True)
    price=models.DecimalField(max_digits=7,decimal_places=2)
    digital=models.BooleanField(default=True,null=True,blank=False)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    image=models.ImageField(null=True,blank=True)
    
    
    class Meta:
            db_table="products"
        
    
    def __str__(self):
        return self.name
    @property
    def imageURL(self):
            try:
                    url=self.image.url
            except:
                    url=''
            return url
    

    
class Order(models.Model):
    codeOrder=models.IntegerField(default=0,null=True,blank=True)
    dateOrdered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False,null=True,blank=False)
    transactionId=models.CharField(max_length=200,null=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
    invoice=models.OneToOneField(Invoice,on_delete=models.CASCADE,null=True,blank=True)
    products= models.ManyToManyField(Product)
    
    
    class Meta:
            db_table="orders"
        
    
    
    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
            orderitems=self.orderitem_set.all()
            total=sum([item.get_total for item in orderitems])
            return total
    @property
    def get_cart_total1(self):
            orderitems=self.orderitem_set.all()
            total=sum([item.get_total for item in orderitems])
            total1=total+5
            return total1
    
    @property
    def get_cart_items(self):
            orderitems=self.orderitem_set.all()
            total=sum([item.quantity for item in orderitems])
            return total
    @property
    def shipping(self):
            shipping=False
            orderitems=self.orderitem_set.all()
            for i in orderitems:
                    if i.product.digital == False:
                        shipping=True
            return shipping
         
                    
    


        
        
class OrderItem(models.Model):
        product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True) 
        order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True,blank=True)
        quantity=models.IntegerField(default=0,null=True,blank=True) 
        date_added=models.DateTimeField(auto_now_add=True)                             
        
        @property
        def get_total(self):
                total=self.product.price * self.quantity
                return total 


class ShippingAdress(models.Model):
        customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
        order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
        address=models.CharField(max_length=200,null=False)
        city=models.CharField(max_length=200,null=False)
        state=models.CharField(max_length=200,null=False)
        zipcode=models.CharField(max_length=200,null=False)
        country=models.CharField(max_length=200,null=False)
        date_added=models.DateTimeField(auto_now_add=True)