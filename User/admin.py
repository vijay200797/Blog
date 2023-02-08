from django.contrib import admin
from User.models import User, Address
# Register your models here.
# admin.site.register(User)
# admin.site.register(Address)

@admin.register(Address)
class Address(admin.ModelAdmin):
    list_display =('id', 'userID','name', 'mobileNo', 'pincode', 'status')
