from django.db import models

# Create your models here.

Status =[
    (0, "In-Active"),
    (1, "Active")
]

class Employee(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    EmailID = models.EmailField(max_length=60)
    EmployeeCode = models.CharField(max_length=8)
    Active = models.IntegerField(choices=Status)

