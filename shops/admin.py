from django.contrib import admin
from .models import Category, SubCategory, Products, Order, OrderItems
# Register your models here.
@admin.register(Category)
class Category(admin.ModelAdmin):
    field="__all__"
    

@admin.register(SubCategory)
class SubCategory(admin.ModelAdmin):
    field="__all__"

@admin.register(Products)
class Products(admin.ModelAdmin):
    field="__all__"
    list_display = ('id', 'name', 'title', 'desc', 'price', 'createdDatetieme', 'publishDatetime', 'active', 'delete', 'category','subcategory','image',  'availbleqty')


# admin.site.register(Order)
# admin.site.register(OrderItems)

@admin.register(Order)
class Order(admin.ModelAdmin):
    field="__all__"
    list_display =('id', 'userID', 'addressID', 'orderAmount', 'createdDatetime', 'paidStaus', 'PaidMode')

@admin.register(OrderItems)
class OrderItems(admin.ModelAdmin):
    field="__all__"
    list_display = ('id', 'orderID', 'productID', 'quantity', 'price')