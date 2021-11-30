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
        return self.name




class Product(models.Model):
    name=models.CharField(max_length=200,null=True)
    price=models.IntegerField()
    digital=models.BooleanField(default=True,null=True,blank=False)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    
    
    class Meta:
            db_table="products"
        
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    codeOrder=models.IntegerField((""))
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
