from django.shortcuts import render
from .models import Products
from math import ceil

# Create your views here.
def vw_Shop(request):
    allProducts=[]
    
    subcatsProduct = Products.objects.values('subcategory','id')
    subcats = {item['subcategory'] for item in subcatsProduct}
    for subcat in subcats:
        prod = Products.objects.filter(subcategory=subcat)
        totalProduct = len(prod)
        nSlides = totalProduct // 4 + ceil((totalProduct/4) -(totalProduct//4))
        allProducts.append([prod, range(0,nSlides), nSlides])
    
    context={
        'allProducts':allProducts
    }
    return render(request, "Shops/index.html",context)

def vw_ProductDetail(request, myid):
    productDetail = Products.objects.filter(id=myid)
    print(productDetail)
    context={
        'product':productDetail[0]
    }
    return render(request, "Shops/ProductDetails.html",context)

def vw_ProductCarts(request):    
    return render(request, "Shops/ProductCarts.html")