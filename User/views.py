from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .form import UserRegistration
from django.contrib import messages


# Create your views here.

def vw_ViewUsers(request):
    return render(request, 'User/view_user.html')
    #return HttpResponse("View Users")

def vw_RegisterUser(request):
    if request.method == "POST":
        frm_UserCreation = UserRegistration(request.POST)
        if frm_UserCreation.is_valid():
            frm_UserCreation.save()
            messages.success(request, "Account Created Successfully !!")
    else:
        frm_UserCreation = UserRegistration()

    return render(request, 'User/register_user.html', {"formReg":frm_UserCreation})
    #return HttpResponse("Register Users")

def vw_LoginUser(request):
    if not request.user.is_authenticated:

        if request.method == "POST":
            frm_UserAuthentication = AuthenticationForm (request=request, data=request.POST)
            if frm_UserAuthentication.is_valid():
                uname = frm_UserAuthentication.cleaned_data['username']
                upass = frm_UserAuthentication.cleaned_data['password']
                user = authenticate(username= uname,password= upass)
                if user is not None:
                    login(request, user=user)
                    messages.success(request, "Logged in Successfully !!")
                    return redirect('/')
        else:
            frm_UserAuthentication = AuthenticationForm()

        return render(request, 'User/login_user.html', {'formLogin': frm_UserAuthentication})
    else:
        return redirect("/")

def vw_ForgetUserID(request):
    return render(request, 'User/forget_user.html')

def vw_LogOutUser(request):
    logout(request = request)
    return render(request, 'User/logout_user.html')