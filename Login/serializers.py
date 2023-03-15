from rest_framework import serializers
from . import models

class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ("id","username", "email","password")
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}}
        }

    def create(self, validated_data):
        user = models.User.objects._create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user
    
    
    
class CompanySerializer(serializers.ModelSerializer):
    created_by=UserSerializer(read_only=True)
    logo=serializers.SerializerMethodField()
    
    class Meta:
        model = models.Company
        fields = ["id","company_name", "created_by","logo","phone","address",'city','zipcode','country','created_at']
        depth=2

    def get_logo(self, obj):
        request = self.context.get('request')
        logo = obj.logo.url
        return request.build_absolute_uri(logo)
