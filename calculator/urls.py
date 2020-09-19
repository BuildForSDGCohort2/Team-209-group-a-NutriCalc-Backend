from django.urls import path
from . import views



urlpatterns = [
    path('', views.index,name='index'),
    # path('user/register', views.register_user,name='registration_endpoint'),
    # path('user/auth', views.authenticate_user,name='authentication_endpoint'),
    path('fertilizers',views.get_fertilizers,name="fertilizer_endpoint"),
    
]
