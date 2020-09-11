from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics, generics
from .serializers import RegisterSerializer, EmailVerifySerializer
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
# Create your views here.

# register APIview


class RegisterView(generics.GenericAPIView):
    serializer_class=RegisterSerializer()
    def post(self,request):
        user=request.user
        serializer=serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data=serializer.validated_data()
        # use saved email to send verifying link
        user=User.objects.get(email=user_data['email.'])
        # give user a token tto verify email
        tokens=RefreshToken.for_user(user=user)
        print(token)
        # link to verify API endpoint
        # endpoint=reverse('verify_endpoint')
        # current site domain
        
        return Response(user_data,status=status.HTTP_201_CREATED)

class VerifyEmailView(generics.GenericAPIView):
    serializer_class=EmailVerifySerializer()
    #  get token
    # set user is_verified status to True
    #