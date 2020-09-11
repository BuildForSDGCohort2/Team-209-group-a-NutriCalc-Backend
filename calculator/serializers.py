
from rest_framework import serializers
from authentication.models import User


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
