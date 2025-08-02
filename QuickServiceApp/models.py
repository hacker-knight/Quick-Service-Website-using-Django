from django.db import models

# Create your models here.
from django.db import models
import random as r

# Create your models here.

class Shop(models.Model):
    shop_name=models.CharField(max_length=200)
    g_map=models.TextField()
    pin=models.IntegerField()
    s_phone=models.CharField(max_length=10)
    uname=models.EmailField(max_length=254,unique=True)
    psw=models.CharField(max_length=10)
    s_cat=models.CharField(max_length=200)
    def __str__(self):
        return self.shop_name

class Categories(models.Model):
    shop_un=models.EmailField(max_length=254)
    cat_name=models.CharField(max_length=200)

    def __str__(self):
        return self.cat_name
    
class Product(models.Model):
    shop_un=models.EmailField(max_length=254)
    prod_cat=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    description=models.TextField()
    cost=models.IntegerField()
    qtn=models.IntegerField(default=1)
    image=models.ImageField(upload_to='images/')
    note=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Client(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    email=models.EmailField(max_length=254,unique=True)
    address=models.TextField()
    pin=models.IntegerField()
    phone=models.CharField(max_length=10)
    psw=models.CharField(max_length=10)

    def __str__(self):
        return self.email

class Orders(models.Model):
    STATUS = (
        ('Cart','Cart'),
        ('Ordered','Ordered'),
        ('Received','Received')
    )
    client=models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    p_s_un=models.EmailField(max_length=254)
    p_c_n=models.CharField(max_length=200)
    p_name=models.CharField(max_length=200)
    p_qtn=models.IntegerField()
    p_deliver=models.CharField(max_length=200, choices=STATUS)
    p_cost=models.IntegerField()

    def __str__(self):
        if self.p_qtn>1:
            self.p_cost=self.p_cost*2
        return self.p_s_un+' '+self.p_name

