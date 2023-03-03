from django.urls import path
from .FunctionBased_api_views import vw_EmployeeFunctionBasedAPI
from .ClassBase_api_views import EmployeeClassBasedView

urlpatterns =[
    path('employeeFunctionBasedAPI/', vw_EmployeeFunctionBasedAPI, name="employee_api" ),
    path("employeeClassBasedAPI/", EmployeeClassBasedView.as_view(), name="employee_class_based_API")
]

