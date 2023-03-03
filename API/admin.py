from django.contrib import admin
from .models import Employee

# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    list_display = ['id', 'FirstName', 'LastName', 'EmailID', 'EmployeeCode','Active']
