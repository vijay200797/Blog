from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vw_ViewUsers(request):
    return render(request, 'User/view_user.html')
    #return HttpResponse("View Users")

def vw_RegisterUser(request):
    return render(request, 'User/register_user.html')
    #return HttpResponse("Register Users")

def vw_LoginUser(request):
    return render(request, 'User/login_user.html')
    #return HttpResponse("Login User")

def vw_ForgetUserID(request):
    return render(request, 'User/forget_user.html')
    #return HttpResponse("Forget User ID")
