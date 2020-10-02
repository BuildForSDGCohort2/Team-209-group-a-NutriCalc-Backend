from django.urls import path
from .views import get_fertilizers, get_plants, FarmView, index,get_farms



urlpatterns = [
    path('', index,name='index'),
    # path('user/register', views.register_user,name='registration_endpoint'),
    # path('user/auth', views.authenticate_user,name='authentication_endpoint'),
    path('fertilizers',get_fertilizers,name="fertilizer_endpoint"),
    path('plants', get_plants, name="plant_endpoint"),
    path('farms', get_farms, name="farms_endpoint"),
    path("farmer/<int:id>/farms",FarmView.as_view(), name="farm's_farms"),
    
]
