from django.urls import path
from . import views
from rest_framework import routers



urlpatterns = [
    path('company/',views.CreateCompanySerializerView.as_view(),name='create_company'),
    path('user/',views.CreateUserSerializerView.as_view(),name='create_user'),
    
    ]