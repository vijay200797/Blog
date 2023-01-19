from django.urls import path

from .views import (  vw_Shop, vw_ProductDetail, vw_ProductCarts  
    )

urlpatterns = [
    path('', vw_Shop, name='viewShops'),
    path('productDetails/<int:myid>', vw_ProductDetail, name='productDetails'),
    path('productCarts/', vw_ProductCarts, name='productCarts')

]
