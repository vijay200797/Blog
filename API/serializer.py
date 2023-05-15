from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta():
        model = Employee
        fields = ['id', 'FirstName', 'LastName', 'EmailID', 'EmployeeCode','Active']

    def validate_EmployeeCode(self, value):
        if len(value)<6:
            raise serializers.ValidationError("Invalid Employee Code")
        return value

    def validate(self, data):
        if len(data["FirstName"])<3 or len(data["LastName"])<3 :
            raise serializers.ValidationError("Required Valid First Name or Last Name")   
        return data

    def create(self, validated_data):
        print("trigger create method")
        return super().create(validated_data)   

    def update(self, instance, validated_data):
        print("trigger update method")
        return super().update(instance, validated_data) 
    
    

