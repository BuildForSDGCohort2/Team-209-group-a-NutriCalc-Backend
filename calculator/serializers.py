
from rest_framework import serializers
from authentication.models import User
from .models import Fertilizer, Plant,Farm


class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "password"]
        extra_kwargs = {'password':
                        {'write_only': True}
                        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(password)
        user.save()
        return user
class FertilizerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Fertilizer
        fields = ["fertilizer_name",]


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ["name", ]


class FarmSerializer(serializers.ModelSerializer):

    class Meta:
        model=Farm
        fields = ['owner', 'farm_name ', 'size_of_land',
                  'location', 'soil_assesment', 'farm_inputs', 'plants']
    pass
