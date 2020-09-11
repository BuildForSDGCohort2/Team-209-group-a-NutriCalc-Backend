from django.urls.conf import path
from .views import RegisterView,VerifyEmailView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path("register", RegisterView.as_view(),name="register_endpoint"),
    path("verify_email", VerifyEmailView.as_view(),name="verify_endpoint"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

