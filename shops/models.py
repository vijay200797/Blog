from django.db import models
from User.models import Address
from django.contrib.auth.models import (
    User
    )

STATUS =[
    (1, "Active"),
    (0, "In Active")
]

Delete =[
    (1, "Deleted"),
    (0, "Not Delete")
]

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)    

    def __str__(self):
        return self.category


class SubCategory(models.Model):
    subCategory = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.subCategory

class Products(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    createdDatetieme = models.DateTimeField(auto_now_add=True)
    publishDatetime = models.DateTimeField(auto_now_add=True)
    active = models.IntegerField(choices=STATUS, default=1)
    delete = models.IntegerField(choices=Delete, default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    image= models.ImageField(upload_to="shop/images", default="")
    availbleqty = models.IntegerField(default=200)
    

    def __str__(self):
        return self.name

PaidStatus =[
    (1, "Paid"),
    (0, "Un-Paid")
]

PaidMode =[
    (1, "Cash on Delivery"),
    (2, "Paytm")
]
class Order(models.Model):
    userID = models.ForeignKey(User, on_delete=models.PROTECT)
    addressID = models.ForeignKey(Address, on_delete=models.PROTECT)
    orderAmount = models.DecimalField(max_digits=20, decimal_places=2)
    createdDatetime = models.DateTimeField(auto_now_add=True)
    paidStaus = models.IntegerField(choices=PaidStatus, default=0)
    PaidMode = models.IntegerField(choices=PaidMode, default=0)

    def __str__(self):
        return str(self.id)

class OrderItems(models.Model):
    orderID = models.ForeignKey(Order, on_delete=models.PROTECT)
    productID = models.ForeignKey(Products, on_delete=models.PROTECT)
    quantity =  models.IntegerField(default=0)
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return str(self.id)