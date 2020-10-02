from django.shortcuts import render
from .serializers import FertilizerSerializer,PlantSerializer,FarmSerializer,FarmerSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.renderers import JSONRenderer
from django.http.response import HttpResponse
from authentication.models import User
from .models import Fertilizer,Plant,Farm,Farmer
from rest_framework import generics, status
from django.contrib.auth import get_user_model

# Create your views here.



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# backend logic views


# api views

'''

API VIEWS: functional api  views

'''
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def get_fertilizers(request):
    if request.method=="GET":
        query = Fertilizer.objects.all()
        serializer_class = FertilizerSerializer(query,many=True)
        return Response(serializer_class.data)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def get_plants(request):
    if request.method == "GET":
        queryset = Plant.objects.all()
        serializer_class = PlantSerializer(queryset, many=True)
        return Response(serializer_class.data)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def get_farms(request):
    if request.method == "GET":
        queryset = Farm.objects.all()
        serializer_class = FarmSerializer(queryset, many=True)
        return Response(serializer_class.data)
    serializer_class = FarmSerializer(data=request.data)
    serializer_class.is_valid(raise_exception=True)
    return Response(serializer_class.data)

class FarmView(generics.GenericAPIView):
    serializer_class=FarmerSerializer
    
    # overriding get queryset
    def get_queryset(self):
        """
        returns farms for the specific user
        """
        queryset = Farmer.objects.all()
        id= self.kwargs['id']
        user = get_user_model().objects.get(pk=id)
        if user is not None:
            return queryset.filter(farm_owner=user)
        
    # get farmer's farms
    def get(self,request,id):
        serializer=self.serializer_class(self.get_queryset(),many=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    # create farm for farmer
    def post(self,request,id):
        data=request.data
        serializer=self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        json=serializer.data
        return Response(json,status=status.HTTP_201_CREATED)


# User Creating Endpoint


# @api_view(['GET', 'POST'])
# @permission_classes([AllowAny])
# def register_user(request):
#     if request.method == "POST":
#         new_user = request.data
#         new_user_username = new_user['username']
#         serializer = UserSerializer(
#               data=new_user, context={'request': request})
#         valid = serializer.is_valid()
#         if valid:
#             print(serializer.validated_data)
#             serializer.save()
#             message = f'new user,{new_user_username}, was added'
#             return Response({'messagee': message, 'status': 200})
#         return Response({"message": "user not added", "status": 404})
#     return Response({'message': "Add a new user"})

#     # User Auth Endpoint


# @api_view(['GET', 'POST'])
# @permission_classes([AllowAny])
# def authenticate_user(request):
#     if request.method == "POST":
#         data = request.data
#         user = User.objects.get(email=data['email'])
#         if user:
#             authenticated_user = authenticate(
#                 request, username=user.username, password=data["password"])
#             if authenticated_user is not None:
#                 serializer = UserSerializer(authenticated_user)
#                 json = JSONRenderer().render(serializer.data)
#                 print(json)
#                 return Response({'user': json, 'status': 200})
#             return Response({"message": "Wrong email or password", "status": 403})
#         return Response({"message": "no such user", "status": 404})
#     return Response({'message': "hello world"})



