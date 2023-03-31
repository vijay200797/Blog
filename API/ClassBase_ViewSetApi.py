from .serializer import EmployeeSerializer
from .models import Employee

from rest_framework.response import Response
from rest_framework import status, viewsets

class EmployeeClass_viewsets(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
