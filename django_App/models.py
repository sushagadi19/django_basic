from django.db import models

# Create your models here.
class Customers(models.Model):
    name= models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    datacreated= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name= models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    STATUS = (('outdor', 'outdoor'),
              ('indoor', 'indoor'))

    name = models.CharField(max_length=100, null=True)
    price = models.FloatField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True,choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS=(('pending','pending'),
            ('out of delevery','out of delevery'),
            ('delevery','delevery'))
    customer =models.ForeignKey(Customers,null=True,on_delete=models.SET_NULL)
    product = models.ForeignKey(Products,null=True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status= models.CharField(max_length=100,null=True,choices=STATUS)

    def __str__(self):
        return self.product.name


