from django.urls import path
from . import views
from rest_framework import routers



urlpatterns = [
    path('createmployee/',views.CreateEmployeeSerializerView.as_view(),name='create_company'),
    path('createasset/',views.CreateAssetSerializerView.as_view(),name='create_asset'),
    path('createdelegation/',views.CreateDelegationSerializerView.as_view(),name='create_delegation'),
    path('get_assets/<uuid:id>/',views.get_all_company_assets,name='get_company_assets'),
    path('get_employee/<uuid:id>/',views.get_all_company_employees,name='get_company_employee'),
    path('get_deligated_assets/<uuid:company>/<uuid:asset>/',views.get_all_delegated_assets,name='get_deligated_assets'),
    ]