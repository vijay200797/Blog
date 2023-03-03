from django.shortcuts import render
from .models import Employee
from .serializer import EmployeeSerializer

from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView

class EmployeeClassBasedView(APIView):

    def get(self, requests, format=None):
        id = requests.data.get("id")
        if id is not None:
            objEmployee = Employee.objects.get(pk=id)
            objSerializer = EmployeeSerializer(objEmployee)
            return Response({'data': objSerializer.data, 'status':status.HTTP_200_OK })
        else:
            objEmployee = Employee.objects.all()
            objSerializer = EmployeeSerializer(objEmployee, many=True)
            return Response({'data': objSerializer.data, 'status':status.HTTP_200_OK })

    def post(self, requests, format=None):
        objSerialize= EmployeeSerializer( data=requests.data)
        if objSerialize.is_valid():
            objSerialize.save()
            return Response({'message':"Success", 'status': status.HTTP_201_CREATED})
        else:
            return Response({'message':objSerialize.errors, 'status': status.HTTP_400_BAD_REQUEST})
    def put(self, requests, format=None):
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

    def delete(self, requests, format=None):
        id = requests.data.get('id')
        objEmployee = Employee.objects.filter(id=id)
        if len(objEmployee)>0:
            objEmployee = Employee.objects.get(pk=id)
            objEmployee.delete()
            return Response({'message': "Resource Deleted", 'status':status.HTTP_200_OK })
        else :
            return Response({'message': "Resource Not Found", 'status':status.HTTP_204_NO_CONTENT })

