from django.shortcuts import render
from . import models,serializers
from rest_framework import viewsets,generics,mixins,response
# Create your views here.
import uuid

class CreateCompanySerializerView(generics.ListCreateAPIView):
    queryset=models.Company.objects.all()
    serializer_class=serializers.CompanySerializer
    def create(self,request,*args,**kwargs):
        print(request.data)
        user=request.data['created_by']
        company_name=request.data['company_name']
        phone=request.data['phone']
        address=request.data['address']
        city=request.data['city']
        zipcode=request.data['zipcode']
        country=request.data['phone']
        created_by=models.User.objects.get(email=user)
        company=models.Company.objects.create(company_name=company_name,phone=phone,address=address,city=city,zipcode
=zipcode,country=country,created_by=created_by)
        if models.Company.objects.filter(company_id=company.company_id):
            company.company_id=uuid.uuid4()
            company.save()
        serializer=serializers.CompanySerializer(company,context={'request':request})
        return response.Response(serializer.data)

# creating company view


    
class CreateUserSerializerView(generics.CreateAPIView):
    queryset=models.User.objects.all()
    serializer_class=serializers.UserSerializer
    
# view to create users who are the owners of their company.