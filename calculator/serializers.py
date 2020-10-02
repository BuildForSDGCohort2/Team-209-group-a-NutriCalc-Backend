
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Fertilizer, Plant,Farm,Area,Farmer
from django.core.exceptions import ValidationError





class FertilizerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Fertilizer
        fields = ["fertilizer_name",]


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ["name", ]

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ["county","area_name",]


class FarmSerializer(serializers.ModelSerializer):
    location = AreaSerializer()
    class Meta:
        model=Farm
        fields = ['name', 'acres',
                  'location', 'soil_assesment', 'farm_inputs', 'plants']
    def validate(self, attrs):
        name=attrs.get("name")
        acres = attrs.get("acres")
        if not name:
            raise ValidationError('Farm must have a name')
        if not acres:
            raise ValidationError('Farm must have acreage')
        return super().validate(attrs)
    def create(self,validated_data):
        location = validated_data.pop("location")
        farm = Farm.objects.create(**validated_data)
        area= Area.objects.create(**location,place=farm)
        return farm



    
class FarmerSerializer(serializers.ModelSerializer):
    farms = FarmSerializer(many=True)
    class Meta:
        model= Farmer
        fields=["farm_owner","farms"]

        def validate(self, attrs):
            farm_owner_id = attrs.get("farm_owner")
            farm_owner = get_user_model().objects.get(pk=farm_owner_id)
            if not farm_owner:
                raise ValidationError('No such user')
            if not farm_owner.is_verified:
                raise ValidationError('Your email has not been verified')
            if not farm_owner.is_active:
                raise ValidationError('Your account is not active')
            return super().validate(attrs)

        def create(self, validated_data):
            farm_owner_id = validated_data.pop("farm_owner")
            farm_owner = get_user_model().objects.get(pk=farm_owner_id)
            farmer = Farmer.objects.create(farm_owner=farm_owner)
            farms_data = validated_data.pop('farms')
            for farm_data in farms_data:
                # acres = farm_data.get('size_of_land')
                # location_data = farm_data.get('location')
                # location = Area.objects.create(location_data)
                # name = farm_data.get('name')
                farm = Farm.objects.create(**farm_data, farmers_farms=farmer)
                print(farm)
                return farm
            return farmer
