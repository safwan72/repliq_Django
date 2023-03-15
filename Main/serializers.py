from rest_framework import serializers
from . import models
from Login.serializers import CompanySerializer

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Employee
        depth=1
        fields='__all__'
        
        
class AssetSerializer(serializers.ModelSerializer):
    company=CompanySerializer()
    class Meta:
        model=models.Assets
        depth=1
        fields='__all__'


class DelegationSerializer(serializers.ModelSerializer):
    employee=EmployeeSerializer()
    company=CompanySerializer()
    class Meta:
        model=models.Delegation
        depth=1
        fields='__all__'

