from .models import Employee
from .serializer import EmployeeSerializer
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView

class ClassBaseGenericMixin(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def get_queryset(self):
    #     ids = [3,4,6,7]
    #     obj = Employee.objects.filter(id__in=ids)
    #     print(obj.query)
    #     return obj


