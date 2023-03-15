from django.shortcuts import render
from . import models,serializers
from Login.models import Company
from rest_framework import viewsets,generics,mixins,response
from rest_framework.response import Response
from rest_framework.decorators import api_view
import uuid
# Create your views here.



# A view to assign employees from the company by using companies id.
class CreateEmployeeSerializerView(generics.ListCreateAPIView):
    queryset=models.Employee.objects.all()
    serializer_class=serializers.EmployeeSerializer
    def create(self,request,*args,**kwargs):
        first_name=request.data['first_name']
        middle_name=request.data['middle_name']
        last_name=request.data['last_name']
        phone=request.data['phone']
        address_1=request.data['address_1']
        city=request.data['city']
        zipcode=request.data['zipcode']
        country=request.data['phone']
        company_id=request.data['company_id']
        employee_company=Company.objects.get(company_id=company_id)
        employee=models.Employee.objects.create(first_name=first_name,middle_name=middle_name,last_name=last_name,phone=phone,address_1=address_1,city=city,zipcode
=zipcode,country=country,employee_company=employee_company,company_id=company_id)
        
        if models.Employee.objects.filter(employee_id=employee.employee_id):
            employee.employee_id=uuid.uuid4()
            employee.save()        
        serializer=serializers.EmployeeSerializer(employee,context={'request':request})
        return response.Response(serializer.data)
    
    



# A view to create assets from companies by posting.
class CreateAssetSerializerView(generics.ListCreateAPIView):
    queryset=models.Assets.objects.all()
    serializer_class=serializers.AssetSerializer
    def create(self,request,*args,**kwargs):
        print(request.data)
        name=request.data['name']
        condition=request.data['condition']
        company=request.data['company']
        company=Company.objects.get(company_id=company)
        newasset=models.Assets.objects.create(name=name,condition=condition,company=company)
        if models.Assets.objects.filter(asset_id=newasset.asset_id):
            newasset.asset_id=uuid.uuid4()
            newasset.save()
        serializer=serializers.AssetSerializer(newasset,context={'request':request})
        return response.Response(serializer.data)



# A view to create a delegation and assigning an asset to a companies employee.
class CreateDelegationSerializerView(generics.ListCreateAPIView):
    queryset=models.Delegation.objects.all()
    serializer_class=serializers.DelegationSerializer
    def create(self,request,*args,**kwargs):
        employee=request.data['employee']
        return_condition=request.data['return_condition']
        asset=request.data['asset']
        company=request.data['company']
        company=Company.objects.get(company_id=company)
        asset=models.Assets.objects.get(asset_id=asset)
        employee=models.Employee.objects.get(employee_company=company,employee_id=employee)
        newdelegation=models.Delegation.objects.create(employee=employee,return_condition=return_condition,company=company,asset=asset)
        serializer=serializers.DelegationSerializer(newdelegation,context={'request':request})
        return response.Response(serializer.data)
    




# A view to get all the assets posted by all the companies.    
@api_view(['GET','POST'])
def get_all_company_assets(request,id):
    company=Company.objects.filter(company_id=id)
    if company:
        company=company[0]
        myassets=models.Assets.objects.filter(company=company)
        if myassets.exists():
            assetserializer=serializers.AssetSerializer(myassets,context={'request': request},many=True)
            return Response({'assets':assetserializer.data})
    else:
        return Response({'assets':False})
        



# A view to get all the employees from a certain company with their details.         
@api_view(['GET','POST'])
def get_all_company_employees(request,id):
    company=Company.objects.filter(company_id=id)
    if company:
        company=company[0]
        employees=models.Employee.objects.filter(employee_company=company)
        if employees.exists():
            employeeserializer=serializers.EmployeeSerializer(employees,context={'request': request},many=True)
            return Response({'employees':employeeserializer.data})
    else:
        return Response({'employees':False})
    
    
# A view to get the delegated assets details using company id and asset id and if not found returns false as response 
@api_view(['GET','POST'])
def get_all_delegated_assets(request,company,asset):
    company=Company.objects.filter(company_id=company)
    if company:
        company=company[0]
        asset=models.Assets.objects.filter(asset_id=asset)
        if asset.exists():
            dass=[]
            asset=asset[0]
            deligated_assets=models.Delegation.objects.filter(company=company,asset=asset)
            print(deligated_assets)
            for m in deligated_assets:
                dass.append(m)
            deligated_assetserializer=serializers.DelegationSerializer(dass,context={'request': request},many=True)
            return Response({'employees':deligated_assetserializer.data})
    else:
        return Response({'employees':False})
    