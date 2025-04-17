from rest_framework import viewsets
from .models import COMPANY,Employee
from .serializers import Companyserializer,Employeeserializer

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = COMPANY.objects.all()
    serializer_class = Companyserializer
    
class Employeeviewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = Employeeserializer
    
    
