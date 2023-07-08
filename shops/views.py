from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
from .models import Products, Order, OrderItems
from .payment.paytm import Checksum
from User.models import Address
from math import ceil
import json

MERCHANT_KEY ="bKMfNxPPf_QdZppa"
MERCHANT_ID = "DIY12386817555501617"
PAYMENT_CALLBACK_URL =  "/shops/handleRequest/"

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

def productMatch(query, item):
    if query.lower() in item.desc.lower() or query.lower() in item.name.lower() or query.lower() in item.title.lower():
        return True


def vw_Search(request):
    query= request.GET.get('product')
    if query is None:
        query=""
    allProducts=[]
    subcatsProduct = Products.objects.values('subcategory','id')
    subcats = {item['subcategory'] for item in subcatsProduct}
    for subcat in subcats:
        prodItems = Products.objects.filter(subcategory=subcat)
        prod = [item for item in prodItems if  productMatch(query, item)]
        totalProduct = len(prod)
        nSlides = totalProduct // 4 + ceil((totalProduct/4) -(totalProduct//4))
        if totalProduct!=0:
            allProducts.append([prod, range(0,nSlides), nSlides])
    
    context={
        'allProducts':allProducts
    }

    print(len(allProducts))
    if len(allProducts)<=0:
        context={
        'Status':'Failed',
        'Message':'No found Search.. please change search cretria '
        }

    print(context)
    return render(request,"Shops/Search.html", context)


def vw_ProductDetail(request, myid):
    productDetail = Products.objects.filter(id=myid)
    # print(productDetail)
    context={
        'product':productDetail[0]
    }
    return render(request, "Shops/ProductDetails.html",context)

def vw_ProductCarts(request):    
    return render(request, "Shops/ProductCarts.html")

def vw_CheckOut(request):    
    if request.user.is_authenticated:
            
        address= Address.objects.filter(userID= request.user) and Address.objects.filter(status= 1)
        # print(address.query)
        context = {
            'address' : address
        }
        return render(request, "Shops/CheckOut.html", context)
    else:
        return redirect("/")

def vw_AddressDelete(request):
    # print(request.method)
    if request.method == "POST":
        hdnAddressID = request.POST.get("hdnDeleteAddressID")
        address = Address.objects.get(id= hdnAddressID)
        address.status=0
        address.save()

    return redirect('/shops/checkOut/')

def vw_SaveAddress(request):
    try:
        if request.method =="POST":
            name = request.POST.get("name")
            mobile_no = request.POST.get("mobile_no")
            pincode = request.POST.get("pincode")
            locality = request.POST.get("locality")

            addressa = request.POST.get("addressDetail")
            citydistricttown = request.POST.get("citydistricttown")
            state = request.POST.get("stateID")
            landmark = request.POST.get("landmark")
            alternatePhone = request.POST.get("alternatePhone", None)
            addressType = request.POST.get("addressType")
            addressA = Address(userID=request.user, 
                            name = name,
                            mobileNo = mobile_no,
                            pincode = pincode,
                            locality = locality,
                            address = addressa,
                            citytown = citydistricttown,
                            state = state,
                            landmark = landmark,
                            alternatephone = alternatePhone,
                            addressType =  addressType
                            )
            addressA.save()
            address = {
                'id': addressA.id,
                'name' : addressA.name,
                'mobileNo' : addressA.mobileNo,
                'pincode' : addressA.pincode,
                'locality' : addressA.locality,
                'address' : addressA.address,
                'citytown' : addressA.citytown,
                'state' : addressA.state,
                'landmark' : addressA.landmark,
                'alternatephone' : addressA.alternatephone,
                'addressType' :  addressA.addressType
            }
            # print(addressA)
            return  HttpResponse(json.dumps({"Status": "Success", "Address":address}))
    except Exception as e:
        print(e)
        return  HttpResponse(json.dumps({"Status": "Failed"}))

@transaction.atomic
def vw_SaveOrder(request):
    try:
        if request.method =="POST":
            cartsItems = request.POST.get("hdnCartsItems")
            addressID = request.POST.get("hdnAddressID")
            totalAmount = request.POST.get("hdnTotalAmmount")
            orderItems = json.loads(cartsItems)

            address = Address.objects.filter(id = addressID)[0]

            order = Order(userID = request.user,
                        addressID = address,
                        orderAmount = totalAmount, 
                        paidStaus =1,
                        PaidMode =1
                        )
            order.save()
            
            for items in orderItems:
                prid= items.get("id")[2:]
                product = Products.objects.filter(id = prid)

                orderitem = OrderItems(
                    orderID = order,
                    productID = product[0],
                    quantity = int(items.get("qty")),
                    price = items.get("price")
                )
                orderitem.save()

            totalAmount = 120.00
            param_dict = {
                'MID':MERCHANT_ID,
                'ORDER_ID': "cxby" + str(order).rjust(6,"0") + "ndv" ,
                'TXN_AMOUNT':str(totalAmount),
                'CUST_ID':"vijay200797ABC@gmail.com",
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID' :'WEB',
                'CALLBACK_URL': request.build_absolute_uri('/')[:-1]+PAYMENT_CALLBACK_URL 

            }
            param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
            return render(request, 'Shops/Paytm.html', {'param_dict': param_dict})

    except Exception as e:
        print(e)
        url ="/shops/message/?messageid={0}&orderid={1}".format(0, None)
        return redirect(url)

def vw_orderSavedMessage(request):
    order_id = request.GET.get('orderid')
    messageid = request.GET.get('messageid')
    context = {}
    if messageid == "1":
        context = {
        'Status' : "Success",
        'OrderID' :  order_id 
        }
    else:
        context = {
        'Status' : "Failed"
        }
    return render(request, "Shops/OrderSubmitMessage.html", context)

@csrf_exempt
def handleRequest(request):
    form = request.POST
    response_dict = {}
    url ="/shops/message/?messageid={0}&orderid={1}".format(0, None)
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
            verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
            if verify:
                if response_dict['RESPCODE'] == '01':
                    url ="/shops/message/?messageid={0}&orderid={1}".format(1, response_dict.get("ORDERID"))
                    print('order successful')
                else:
                    print('order was not successful because' + response_dict['RESPMSG'])

                # Write Code To Save Payment Details

    return redirect(url)
