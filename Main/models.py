from django.db import models
import uuid
from Login.models import Company
# Create your models here.



class Employee(models.Model):
    first_name=models.CharField(max_length=264)
    middle_name=models.CharField(max_length=264,blank=True)
    last_name=models.CharField(max_length=264)
    address_1=models.TextField(max_length=264,blank=True)
    city=models.CharField(max_length=40,blank=True)
    zipcode=models.CharField(max_length=10,blank=True)
    country=models.CharField(max_length=40,blank=True)
    phone=models.CharField(max_length=20)
    date_joined=models.DateTimeField(auto_now_add=True)
    company_id=models.CharField(max_length=60)
    employee_company=models.ForeignKey(Company, related_name='employee_company', on_delete=models.CASCADE)
    employee_id=models.CharField(max_length=100,default=uuid.uuid4,unique=True)
        
    class Meta:
        verbose_name_plural = "Employee"
        db_table = "Employee"

    def __str__(self):
        return self.first_name+" "+self.last_name+"  "+str((uuid.uuid4()))


CONDITIONS = (
        ('New', 'New'),
        ('Used', 'Used'),
    )


class Assets(models.Model):
    name=models.CharField(max_length=60)
    condition=models.CharField(max_length=40,choices=CONDITIONS,default=CONDITIONS[0][0])
    check_in=models.DateTimeField(auto_now_add=True)
    company=models.ForeignKey(Company,on_delete=models.CASCADE,related_name='customer')
    asset_id=models.CharField(max_length=100,default=uuid.uuid4,unique=True)
    
    class Meta:
        verbose_name_plural = "Assets"
        db_table = "Assets"

    def __str__(self):
        return self.name+" added by "+self.company.company_name
    
    
class Delegation(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    return_condition=models.CharField(max_length=40,choices=CONDITIONS,default=CONDITIONS[1][1])
    return_date=models.DateTimeField(auto_now_add=True)
    asset=models.ForeignKey(Assets,on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Delegation"
        db_table = "Delegation"

    def __str__(self):
        return "Employee ID -"+self.employee.employee_id + "delegation for Asset Number -"+self.asset.asset_id