from django.urls import path

from .views import (  vw_Shop, vw_ProductDetail, vw_ProductCarts, vw_CheckOut, vw_SaveAddress, \
      vw_SaveOrder, vw_orderSavedMessage, handleRequest, vw_AddressDelete
    )

urlpatterns = [
    path('', vw_Shop, name='viewShops'),
    path('productDetails/<int:myid>', vw_ProductDetail, name='productDetails'),
    path('productCarts/', vw_ProductCarts, name='productCarts'),
    path('checkOut/', vw_CheckOut, name='checkOuts'),
    path('saveAddress/', vw_SaveAddress, name='saveAddress'),
    path('deleteAddress/', vw_AddressDelete, name='deleteAddress'),
    path('saveOrder/', vw_SaveOrder, name='saveOrder'),
    path('message/', vw_orderSavedMessage, name='message'),
    path('handleRequest/', handleRequest, name='handleRequest')
]
