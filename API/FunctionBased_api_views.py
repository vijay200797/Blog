from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Employee
from shops.models import Products, Category
from .serializer import EmployeeSerializer

# Function Based API View
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def vw_EmployeeFunctionBasedAPI(requests):
    if requests.method == "GET":
        id = requests.data.get('id')
        if id is not None:
            objEmployee = Employee.objects.get(pk=id)
            objSerial= EmployeeSerializer(objEmployee)
            return Response({'data': objSerial.data, 'status':status.HTTP_200_OK })
        else :
            objEmployee = Employee.objects.all()
            objSerial= EmployeeSerializer(objEmployee, many=True)
            return Response({'data': objSerial.data, 'status':status.HTTP_200_OK })
    if requests.method =="POST":
        objSerialize= EmployeeSerializer( data=requests.data)
        if objSerialize.is_valid():
            objSerialize.save()
            return Response({'message':"Success", 'status': status.HTTP_201_CREATED})
        else:
            return Response({'message':objSerialize.errors, 'status': status.HTTP_400_BAD_REQUEST})
    if requests.method == "DELETE":
        id = requests.data.get('id')
        objEmployee = Employee.objects.filter(id=id)
        if len(objEmployee)>0:
            objEmployee = Employee.objects.get(pk=id)
            objEmployee.delete()
            return Response({'message': "Resource Deleted", 'status':status.HTTP_200_OK })
        else :
            return Response({'message': "Resource Not Found", 'status':status.HTTP_204_NO_CONTENT })

    if requests.method == "PUT":
        id = requests.data.get('id')
        objEmployee = Employee.objects.filter(id=id)
        if len(objEmployee)>0:
            objEmployee = Employee.objects.get(pk=id)
            objSerialize = EmployeeSerializer(instance=objEmployee, data=requests.data)
            if objSerialize.is_valid():
                objSerialize.save()
                return Response({'message': "Resource Updated", 'status':status.HTTP_200_OK })
            else:
                return Response({'message': objSerialize.errors, 'status':status.HTTP_400_BAD_REQUEST})
        else :
            return Response({'message': "Resource Not Found", 'status':status.HTTP_204_NO_CONTENT })        