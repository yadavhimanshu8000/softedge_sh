from rest_framework import serializers
from api.models import COMPANY,Employee

class Companyserializer(serializers.ModelSerializer):
    class Meta:
        model = COMPANY
        fields = '__all__'
        
class Employeeserializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
        