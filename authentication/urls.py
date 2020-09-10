from django.urls.conf import path
from .views import RegisterView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path("register", RegisterView.as_view(),name="register_endpoint"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

