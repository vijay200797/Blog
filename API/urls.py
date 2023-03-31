from django.urls import path, include
from .FunctionBased_api_views import vw_EmployeeFunctionBasedAPI
from .ClassBase_api_views import EmployeeClassBasedView
from .ClassBase_ViewSetApi import EmployeeClass_viewsets
from rest_framework.routers import DefaultRouter

from .GenericApiViewMexin import ClassBaseGenericMixin


objDefaultRauter = DefaultRouter()
objDefaultRauter.register("viewset_api", EmployeeClass_viewsets, basename="viewsetapi")

urlpatterns =[
    path('employeeFunctionBasedAPI/', vw_EmployeeFunctionBasedAPI, name="employee_api" ),
    path("employeeClassBasedAPI/", EmployeeClassBasedView.as_view(), name="employee_class_based_API"),
    path("employeeViewSetAPI/", include(objDefaultRauter.urls)),
    path("employeeClassGenericAPIMixin/", ClassBaseGenericMixin.as_view(), name='employee_class_generic_API_Mixin')
]

