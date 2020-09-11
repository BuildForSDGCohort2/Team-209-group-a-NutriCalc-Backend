from rest_framework import serializers
from .models import User
from django.core.exceptions import ValidationError

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=60,min_length=4, write_only=True)
    class Meta:
        model=User
        fields=['email,username','password']
    def validate(self,attr):
        email=attr.get('email')
        username=attr.get('username')
        password=attr.get('password')
      
        if not username.alnum():
            raise ValidationError('Username must contain only alphanumeric')
        return attr
    def create(self,validated_data):
        return User.objects.create(**validated_data)

class EmailVerifySerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','token']

        def validate():
            pass
