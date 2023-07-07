from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms

class UserRegistration(UserCreationForm):
    username = forms.CharField(label="User Name", widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label="First Name", widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label="Email Address", widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'email']
        
    
class UserLogin(AuthenticationForm):
    username = forms.CharField(label="User Name", widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    