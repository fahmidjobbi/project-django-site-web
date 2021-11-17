from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Client(models.Model):
    name=CharField(max_length=200)
    email=models.EmailField()
    birthDate=models.DateField()
    
    class Meta:
        db_table="clients"
        
    
    
    