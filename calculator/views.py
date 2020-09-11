from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.renderers import JSONRenderer
from django.http.response import HttpResponse
from authentication.models import User

# Create your views here.



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# backend logic views


# api views

'''

API VIEWS: functional api  views

'''

    # User Creating Endpoint


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def register_user(request):
    if request.method == "POST":
        new_user = request.data
        new_user_username = new_user['username']
        serializer = UserSerializer(
              data=new_user, context={'request': request})
        valid = serializer.is_valid()
        if valid:
            print(serializer.validated_data)
            serializer.save()
            message = f'new user,{new_user_username}, was added'
            return Response({'messagee': message, 'status': 200})
        return Response({"message": "user not added", "status": 404})
    return Response({'message': "Add a new user"})

    # User Auth Endpoint


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def authenticate_user(request):
    if request.method == "POST":
        data = request.data
        user = User.objects.get(email=data['email'])
        if user:
            authenticated_user = authenticate(
                request, username=user.username, password=data["password"])
            if authenticated_user is not None:
                serializer = UserSerializer(authenticated_user)
                json = JSONRenderer().render(serializer.data)
                print(json)
                return Response({'user': json, 'status': 200})
            return Response({"message": "Wrong email or password", "status": 403})
        return Response({"message": "no such user", "status": 404})
    return Response({'message': "hello world"})
